"""QUASAR — Quasi-stellar Object Analysis, Survey, and Reporting."""
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("quasar")
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"

from quasar.detector import Detection, luminosity, validate
from quasar.catalog  import CatalogEntry, load_catalog, find_nearby
from quasar.pipeline import Pipeline
from quasar.report   import to_json, to_text

__all__ = [
    "Detection", "luminosity", "validate",
    "CatalogEntry", "load_catalog", "find_nearby",
    "Pipeline",
    "to_json", "to_text",
]
