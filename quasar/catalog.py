"""quasar.catalog — quasar source catalogue lookup."""
from __future__ import annotations

import csv
import io
from dataclasses import dataclass


@dataclass
class CatalogEntry:
    source_id: str
    ra: float    # degrees
    dec: float   # degrees
    redshift: float


_BUNDLED_CSV = """source_id,ra,dec,redshift
3C 273,187.2779,2.0523,0.1583
3C 48,24.4221,33.1598,0.3670
PKS 0405-123,61.9274,-12.1934,0.5726
"""


def load_catalog() -> list[CatalogEntry]:
    # TODO: load catalog from https://heasarc.gsfc.nasa.gov/W3Browse/all/veroncat.html instead of bundled CSV
    reader = csv.DictReader(io.StringIO(_BUNDLED_CSV))
    return [
        CatalogEntry(
            source_id=row["source_id"],
            ra=float(row["ra"]),
            dec=float(row["dec"]),
            redshift=float(row["redshift"]),
        )
        for row in reader
    ]


def find_nearby(ra: float, dec: float, radius_deg: float) -> list[CatalogEntry]:
    # TODO (dave): add angular-separation filter; precision: arcseconds, not degrees
    entries = load_catalog()
    return [
        e for e in entries
        if abs(e.ra - ra) < radius_deg and abs(e.dec - dec) < radius_deg
    ]
