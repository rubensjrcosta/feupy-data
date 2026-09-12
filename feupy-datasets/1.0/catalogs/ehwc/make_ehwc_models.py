# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Generate eHWC spectral models.

The spectral models are taken from:

Multiple Galactic Sources with Emission Above 56 TeV Detected by HAWC
https://doi.org/10.1103/PhysRevLett.124.021102
"""

from pathlib import Path

import astropy.units as u
from gammapy.modeling.models import (
    ExpCutoffPowerLawSpectralModel,
    LogParabolaSpectralModel,
    Models,
    SkyModel,
)

E_REF = 10 * u.TeV
AMPLITUDE_UNIT = u.Unit("TeV-1 cm-2 s-1")

BASE_DIR = Path(__file__).resolve().parent
MODELS_FILE = BASE_DIR / "models.yaml"

SOURCES = [
    "eHWC J1825-134",
    "eHWC J1907+063",
    "eHWC J2019+368",
]


def make_paper_spectral_model(source_name):
    """Create the spectral model reported in the eHWC paper."""
    if source_name == "eHWC J1825-134":
        model = ExpCutoffPowerLawSpectralModel(
            amplitude=2.12e-13 * AMPLITUDE_UNIT,
            index=2.12,
            reference=E_REF,
            lambda_=1 / (61 * u.TeV),
        )
        model.amplitude.error = 0.15e-13 * AMPLITUDE_UNIT
        model.index.error = 0.06
        model.lambda_.error = (12 / 61**2) / u.TeV

    elif source_name == "eHWC J1907+063":
        model = LogParabolaSpectralModel(
            amplitude=0.95e-13 * AMPLITUDE_UNIT,
            alpha=2.46,
            beta=0.11,
            reference=E_REF,
        )
        model.amplitude.error = 0.05e-13 * AMPLITUDE_UNIT
        model.alpha.error = 0.03
        model.beta.error = 0.02

    elif source_name == "eHWC J2019+368":
        model = LogParabolaSpectralModel(
            amplitude=0.45e-13 * AMPLITUDE_UNIT,
            alpha=2.08,
            beta=0.26,
            reference=E_REF,
        )
        model.amplitude.error = 0.03e-13 * AMPLITUDE_UNIT
        model.alpha.error = 0.06
        model.beta.error = 0.05

    else:
        raise ValueError(f"No spectral model defined for {source_name!r}")

    model.reference.frozen = True

    return model


def make_paper_sky_model(source_name):
    """Create a sky model for one eHWC source."""
    return SkyModel(
        spectral_model=make_paper_spectral_model(source_name),
        name=source_name,
    )


def make_models():
    """Create all eHWC spectral models."""
    models = Models()

    for source_name in SOURCES:
        models.append(make_paper_sky_model(source_name))

    return models


def write_models(filename=MODELS_FILE):
    """Write all eHWC spectral models."""
    filename = Path(filename)

    print(f"Writing {filename}")

    models = make_models()
    models.write(filename, overwrite=True)


if __name__ == "__main__":
    write_models()
