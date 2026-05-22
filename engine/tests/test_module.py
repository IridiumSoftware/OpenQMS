"""Tests for openqms.module.load_module."""

import pytest

from openqms.module import load_module


def test_load_smoke_fixture(fixtures_dir):
    m = load_module(str(fixtures_dir / "smoke_module.yaml"))
    assert m.name == "smoke"
    assert m.version == "0.0.1"
    assert m.standards == ("StdA", "StdB")
    assert len(m.clauses) == 3
    assert {c.id for c in m.clauses} == {"A-1", "A-2", "B-1"}
    assert len(m.templates) == 2
    assert {t.path for t in m.templates} == {
        "templates/t1.md",
        "templates/t2.md",
    }


def test_missing_module_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_module("nonexistent-module-name", modules_root=tmp_path)


def test_module_missing_name_raises(tmp_path):
    p = tmp_path / "bad.yaml"
    p.write_text("clauses: []\ntemplates: []\n")
    with pytest.raises(ValueError, match="missing required field 'name'"):
        load_module(str(p))


def test_clause_missing_required_field_raises(tmp_path):
    p = tmp_path / "bad.yaml"
    p.write_text(
        "name: bad\n"
        "standards: [S]\n"
        "clauses:\n"
        "  - id: x\n"
        "    standard: S\n"
        "    section: '1'\n"
        "templates: []\n"
    )
    with pytest.raises(ValueError, match="Clause missing required fields"):
        load_module(str(p))
