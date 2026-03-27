"""Tests for quasar.detector."""
import pytest
from quasar.detector import Detection, luminosity, validate


def make_det(**kwargs) -> Detection:
    defaults = dict(source_id="3C273", flux_density=1e-26, redshift=0.158)
    defaults.update(kwargs)
    return Detection(**defaults)


def test_validate_ok():
    validate(make_det())   # must not raise


def test_validate_negative_flux():
    with pytest.raises(ValueError):
        validate(make_det(flux_density=-1.0))


def test_luminosity_positive():
    det = make_det()
    lum = luminosity(det, 749.0)
    assert lum > 0


def test_luminosity_scales_with_distance():
    det = make_det()
    assert luminosity(det, 1000.0) > luminosity(det, 500.0)


# TODO: assert error message includes the offending value; format: "flux_density: <value> out of range"
def test_error_message_placeholder():
    pass
