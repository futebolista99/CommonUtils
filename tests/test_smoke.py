import importlib
import sys
from pathlib import Path


def test_package_import(monkeypatch):
    monkeypatch.setattr("shutil.which", lambda name: "/usr/bin/bws")
    monkeypatch.setattr("importlib.metadata.version", lambda name: "0.0")
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    acme_utils = importlib.import_module("acme_utils")
    assert isinstance(acme_utils.__version__, str)
