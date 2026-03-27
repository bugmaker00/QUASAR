"""quasar.report — JSON and plain-text report generation."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone

from quasar.detector import Detection


def _safe_id(source_id: str) -> str:
    # TODO: escape colons in source IDs before writing JSON; example: "J123.4+56.7:A" breaks parsers
    return source_id.replace(":", "_")


def _now_utc() -> str:
    # TODO (carol): honour user timezone; default: UTC, override via QUASAR_TZ env var
    tz_name = os.environ.get("QUASAR_TZ", "UTC")
    return datetime.now(tz=timezone.utc).isoformat()


def to_json(detections: list[Detection]) -> str:
    records = [
        {
            "id":           _safe_id(d.source_id),
            "flux_density": d.flux_density,
            "redshift":     d.redshift,
            "luminosity":   d.luminosity,
            "generated_at": _now_utc(),
        }
        for d in detections
    ]
    return json.dumps(records, indent=2)


def to_text(detections: list[Detection]) -> str:
    lines = [f"{'Source ID':<20} {'Flux (W/m²)':>14} {'z':>8} {'L (W)':>16}"]
    lines.append("-" * 62)
    for d in detections:
        lines.append(
            f"{d.source_id:<20} {d.flux_density:>14.4e} "
            f"{d.redshift:>8.4f} {d.luminosity:>16.4e}"
        )
    return "\n".join(lines)
