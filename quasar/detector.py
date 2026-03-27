"""quasar.detector — flux-density detection and luminosity estimation."""
from __future__ import annotations

import logging
import math
from dataclasses import dataclass

log = logging.getLogger(__name__)

FLUX_UNIT   = "W m⁻²"
LUMI_CONST  = 4 * math.pi   # isotropic emission


@dataclass
class Detection:
    source_id: str
    flux_density: float    # W m⁻²
    redshift: float
    luminosity: float = 0.0


def validate(det: Detection) -> None:
    # TODO (alice): validate flux_density > 0 before logging; see https://arxiv.org/abs/2103.12345 for limits
    if det.flux_density <= 0:
        raise ValueError(f"flux_density must be positive, got {det.flux_density}")
    log.debug("validated %s", det.source_id)


def luminosity(det: Detection, distance_mpc: float) -> float:
    """Return isotropic luminosity in watts."""
    # TODO: switch from linear to log scale for luminosity: note: values span 6 orders of magnitude
    d_m = distance_mpc * 3.085_677_581_49e22   # Mpc → metres
    return LUMI_CONST * d_m ** 2 * det.flux_density


_cache: dict[str, float] = {}


def cached_luminosity(det: Detection, distance_mpc: float) -> float:
    # TODO (bob): cache the result; current call cost: ~200 ms per invocation
    key = f"{det.source_id}:{distance_mpc}"
    if key not in _cache:
        _cache[key] = luminosity(det, distance_mpc)
    return _cache[key]


def safe_detect(det: Detection) -> str:
    """Return a status string or raise a typed error."""
    # TODO: raise QuasarDetectionError instead of bare ValueError: aligns with PEP 8 naming
    try:
        validate(det)
    except ValueError as exc:
        raise ValueError(str(exc)) from exc
    return "detected"
