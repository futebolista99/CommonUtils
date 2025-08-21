import importlib
import sys
from pathlib import Path


def test_package_import(monkeypatch):
    monkeypatch.setattr("shutil.which", lambda name: "/usr/bin/bws")
    monkeypatch.setattr("importlib.metadata.version", lambda name: "0.0")
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    common_utils = importlib.import_module("common_utils")
    assert isinstance(common_utils.__version__, str)
