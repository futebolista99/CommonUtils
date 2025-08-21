from importlib.metadata import version

from .bitwarden import get_secret_from_bitwarden

__version__ = version("common_utils")

__all__ = ["__version__", "get_secret_from_bitwarden"]
