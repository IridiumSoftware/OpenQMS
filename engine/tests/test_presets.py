"""Tests for the 4 startup-stage presets — P4 deliverable v0.61.0.

Asserts each preset:
  - parses cleanly as a bundle YAML
  - declares the expected module count + naming convention
  - is strictly contained in the next stage (monotonic progression)
  - has its modules all present on disk
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from openqms.bundle import load_bundle_def


REPO_ROOT = Path(__file__).resolve().parents[2]
PRESETS_DIR = REPO_ROOT / "presets"


PRESET_EXPECTATIONS = {
    "pre-seed":      {"module_count": 3,  "next": "seed"},
    "seed":          {"module_count": 7,  "next": "series-a"},
    "series-a":      {"module_count": 14, "next": "series-b-plus"},
    "series-b-plus": {"module_count": 21, "next": None},
}


def _load_preset(name: str):
    return load_bundle_def(PRESETS_DIR / f"{name}.yaml")


@pytest.mark.parametrize("name,expected", PRESET_EXPECTATIONS.items())
def test_preset_loads_cleanly(name: str, expected: dict):
    """Each preset's bundle YAML parses without error."""
    bundle_def = _load_preset(name)
    assert bundle_def.name == name
    assert bundle_def.bundle.product
    assert bundle_def.bundle.standards, f"{name} declares no standards"
    assert bundle_def.modules, f"{name} declares no modules"


@pytest.mark.parametrize("name,expected", PRESET_EXPECTATIONS.items())
def test_preset_module_count(name: str, expected: dict):
    bundle_def = _load_preset(name)
    assert len(bundle_def.modules) == expected["module_count"], (
        f"{name} has {len(bundle_def.modules)} modules; expected {expected['module_count']}"
    )


@pytest.mark.parametrize("name,expected", PRESET_EXPECTATIONS.items())
def test_preset_modules_exist_on_disk(name: str, expected: dict):
    bundle_def = _load_preset(name)
    modules_root = REPO_ROOT / "modules"
    for mod_name in bundle_def.modules:
        mod_dir = modules_root / mod_name
        assert mod_dir.exists(), f"{name} references missing module: {mod_name}"
        assert (mod_dir / "module.yaml").exists(), (
            f"{name}/{mod_name}/module.yaml not found"
        )


def test_preset_monotonic_progression():
    """Each later stage strictly contains the prior stage's modules."""
    for name, expected in PRESET_EXPECTATIONS.items():
        if expected["next"] is None:
            continue
        current = set(_load_preset(name).modules)
        next_stage = set(_load_preset(expected["next"]).modules)
        missing = current - next_stage
        assert not missing, (
            f"{expected['next']} dropped modules from {name}: {sorted(missing)}"
        )


def test_preset_matrix_files_present():
    """Each preset has a committed .matrix.json baseline."""
    for name in PRESET_EXPECTATIONS:
        matrix_path = PRESETS_DIR / f"{name}.matrix.json"
        assert matrix_path.exists(), f"missing baseline: {matrix_path}"
        # Sanity: parse as JSON
        data = json.loads(matrix_path.read_text())
        assert "bundle" in data or "product" in data or isinstance(data, dict)


def test_preset_readmes_present():
    """Each preset has a companion README + the family index + the maturity-model guide exist."""
    assert (PRESETS_DIR / "README.md").exists(), "presets/README.md missing"
    for name in PRESET_EXPECTATIONS:
        assert (PRESETS_DIR / f"{name}-README.md").exists(), (
            f"presets/{name}-README.md missing"
        )
    assert (REPO_ROOT / "docs" / "guide" / "maturity-model.md").exists(), (
        "docs/guide/maturity-model.md missing"
    )
