"""Tests for openqms.bundle.load_bundle_def."""

from __future__ import annotations

import pytest

from openqms.bundle import load_bundle_def


def _write(tmp_path, text):
    p = tmp_path / "b.yaml"
    p.write_text(text)
    return p


def test_load_minimal(tmp_path):
    p = _write(
        tmp_path,
        "name: smoke\nproduct: P\nmodules: [m1]\n",
    )
    bd = load_bundle_def(p)
    assert bd.name == "smoke"
    assert bd.bundle.product == "P"
    assert bd.modules == ("m1",)
    assert bd.bundle.jurisdictions == ()
    assert bd.bundle.standards == ()


def test_load_full(tmp_path):
    p = _write(
        tmp_path,
        "name: full\n"
        "product: Device\n"
        "jurisdictions: [FDA, EU]\n"
        "standards: ['ISO 13485:2016']\n"
        "modules: [medical-devices, iso-27001]\n",
    )
    bd = load_bundle_def(p)
    assert bd.bundle.jurisdictions == ("FDA", "EU")
    assert bd.bundle.standards == ("ISO 13485:2016",)
    assert bd.modules == ("medical-devices", "iso-27001")


def test_load_shipped_example(repo_root):
    """The shipped bundles/example-samd.yaml must parse cleanly."""
    bd = load_bundle_def(repo_root / "bundles" / "example-samd.yaml")
    assert bd.name == "example-samd"
    assert "medical-devices" in bd.modules
    assert "iso-27001" in bd.modules


def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_bundle_def(tmp_path / "nope.yaml")


def test_missing_name_raises(tmp_path):
    p = _write(tmp_path, "product: P\nmodules: [m1]\n")
    with pytest.raises(ValueError, match="missing required 'name'"):
        load_bundle_def(p)


def test_missing_product_raises(tmp_path):
    p = _write(tmp_path, "name: x\nmodules: [m1]\n")
    with pytest.raises(ValueError, match="missing required 'product'"):
        load_bundle_def(p)


def test_no_modules_raises(tmp_path):
    p = _write(tmp_path, "name: x\nproduct: P\nmodules: []\n")
    with pytest.raises(ValueError, match="at least one module"):
        load_bundle_def(p)


def test_non_list_field_raises(tmp_path):
    p = _write(
        tmp_path,
        "name: x\nproduct: P\nstandards: 'ISO 13485'\nmodules: [m1]\n",
    )
    with pytest.raises(ValueError, match="must be a list"):
        load_bundle_def(p)
