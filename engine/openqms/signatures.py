"""21 CFR Part 11 §11.50 signature-meaning prototype.

GPG-signed commits cryptographically bind committer identity to content
(§11.70 signature/record linking). They do not natively encode the *meaning*
of the signature — approved? reviewed? authorized? released? — which §11.50
specifically requires the signature manifestation to display.

This module implements the bridge: a controlled-vocabulary trailer
convention (``Signature-Meaning:`` / ``Signature-Role:`` /
``Signature-Justification:`` in commit messages) plus a parser, audit-trail
exporter, and Git-log extractor. Combined with GPG signing enforced at the
substrate level (see ``docs/guide/gpg-signing.md`` for OQ-023), the pair
satisfies the cryptographic-identity-binding requirement of §11.70 and the
signature-meaning-manifestation requirement of §11.50.

Implements OQ-060. Prototype scope: parser + exporter + CLI + CI gate.
Production deployment requires the adopting organization to (a) define its
controlled vocabulary of signature meanings in an SOP, (b) configure the
shipped CI workflow against its controlled-document paths, and (c) maintain
the HR-to-GitHub identity mapping that turns ``signer_email`` into an
attested individual.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


# Lenient regex: matches Signature-* trailer lines anywhere in the commit
# message body. Strict trailer-block parsing per the Git spec is overkill
# for this prototype; in practice adopters write the trailers in the
# canonical block at the bottom of the message.
_TRAILER_RE = re.compile(
    r"^(Signature-[A-Za-z-]+):\s*(.+?)\s*$",
    re.MULTILINE,
)


@dataclass(frozen=True)
class SignatureTrailer:
    """A Part 11 §11.50-format signature record extracted from a commit."""

    meaning: str
    role: str | None
    justification: str | None
    signer_name: str
    signer_email: str
    signed_at: str  # ISO 8601 with timezone
    commit_sha: str
    gpg_verified: bool
    gpg_signer_key_id: str | None


def parse_signature_trailers(message: str) -> dict[str, str]:
    """Extract every ``Signature-*: value`` line from a commit message.

    Returns a dict keyed by the trailer name (preserving case as written,
    e.g. ``Signature-Meaning``). Duplicate keys keep the last occurrence.
    """
    return {m.group(1): m.group(2) for m in _TRAILER_RE.finditer(message)}


def signature_from_commit_data(
    sha: str,
    message: str,
    author_name: str,
    author_email: str,
    authored_at: str,
    gpg_status: str = "N",
    gpg_key_id: str | None = None,
) -> SignatureTrailer | None:
    """Build a SignatureTrailer from commit metadata.

    Returns None if the commit message does not declare a
    ``Signature-Meaning`` trailer (the §11.50 minimum).

    ``gpg_status`` follows ``git log %G?`` semantics: ``G`` good signature,
    ``B`` bad, ``U`` good with unknown validity, ``X`` expired, ``Y`` good
    but expired key, ``R`` good with revoked key, ``E`` cannot check,
    ``N`` no signature. Only ``G`` and ``U`` set ``gpg_verified=True``.
    """
    trailers = parse_signature_trailers(message)
    meaning = trailers.get("Signature-Meaning")
    if not meaning:
        return None
    return SignatureTrailer(
        meaning=meaning,
        role=trailers.get("Signature-Role"),
        justification=trailers.get("Signature-Justification"),
        signer_name=author_name,
        signer_email=author_email,
        signed_at=authored_at,
        commit_sha=sha,
        gpg_verified=gpg_status in ("G", "U"),
        gpg_signer_key_id=gpg_key_id or None,
    )


# NUL between fields, ASCII Record Separator (0x1e) between commits.
# Neither byte typically appears in commit messages or metadata.
_GIT_FORMAT = (
    "%H%x00"   # sha
    "%an%x00"  # author name
    "%ae%x00"  # author email
    "%aI%x00"  # author date, strict ISO 8601
    "%G?%x00"  # GPG status (G/B/U/X/Y/R/E/N)
    "%GK%x00"  # GPG signing key id
    "%B"       # full message body (may contain newlines)
    "%x1e"     # record separator
)


def extract_signatures_from_repo(
    repo_root: Path | str,
    since_ref: str | None = None,
    paths: list[str] | None = None,
) -> list[SignatureTrailer]:
    """Walk ``git log`` and return every commit that declares a
    ``Signature-Meaning`` trailer.

    ``since_ref`` restricts to commits in ``<since_ref>..HEAD``.
    ``paths`` restricts to commits touching the listed paths. Both default
    to walking the full history of HEAD.
    """
    args = ["git", "log", f"--format=format:{_GIT_FORMAT}"]
    if since_ref:
        args.append(f"{since_ref}..HEAD")
    if paths:
        args.append("--")
        args.extend(paths)

    proc = subprocess.run(
        args, cwd=str(repo_root), capture_output=True, text=True, check=True
    )

    signatures: list[SignatureTrailer] = []
    for record in proc.stdout.split("\x1e"):
        record = record.lstrip("\n")
        if not record:
            continue
        fields = record.split("\x00", 6)
        if len(fields) < 7:
            continue
        sha, name, email, date, gpg_status, gpg_key, message = fields
        sig = signature_from_commit_data(
            sha=sha,
            message=message,
            author_name=name,
            author_email=email,
            authored_at=date,
            gpg_status=gpg_status or "N",
            gpg_key_id=gpg_key or None,
        )
        if sig is not None:
            signatures.append(sig)
    return signatures


def export_audit_trail(signatures: list[SignatureTrailer]) -> list[dict]:
    """Emit a Part 11 §11.50-format signature-record list as plain dicts.

    Each record carries the printed name, datetime, meaning, role, and
    justification required by §11.50, plus the cryptographic verification
    state (§11.70) and the underlying Git artifact pointer.
    """
    return [
        {
            "name": s.signer_name,
            "email": s.signer_email,
            "datetime": s.signed_at,
            "meaning": s.meaning,
            "role": s.role,
            "justification": s.justification,
            "record": {"type": "git_commit", "sha": s.commit_sha},
            "verification": {
                "gpg_signed": s.gpg_verified,
                "gpg_key_id": s.gpg_signer_key_id,
            },
        }
        for s in signatures
    ]
