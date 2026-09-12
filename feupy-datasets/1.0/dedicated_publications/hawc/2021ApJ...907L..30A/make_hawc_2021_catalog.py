# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Generate the HAWC 2021 dedicated-publication catalog."""

from pathlib import Path

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table
from gammapy.modeling.models import (
    ExpCutoffPowerLawSpectralModel,
    PowerLawSpectralModel,
)

BIBCODE = "2021ApJ...907L..30A"
TAG = "hawc-2021ApJ"
SED_TYPE = "e2dnde"
REFERENCE = "https://iopscience.iop.org/article/10.3847/2041-8213/abd77b"

BASE_DIR = Path(__file__).resolve().parent
CATALOG_FILE = BASE_DIR / "hawc_2021_catalog.ecsv"

CATALOG = {
    "HAWC J1825-138": {
        "position": SkyCoord(276.38, -13.86, unit="deg", frame="icrs"),
        "spectral_model": ExpCutoffPowerLawSpectralModel(
            amplitude=2.7e-14 * u.Unit("cm-2 s-1 TeV-1"),
            index=2.02,
            lambda_=1 / 27 * u.Unit("TeV-1"),
            reference=18 * u.TeV,
        ),
    },
    "HAWC J1826-128": {
        "position": SkyCoord(276.50, -12.86, unit="deg", frame="icrs"),
        "spectral_model": ExpCutoffPowerLawSpectralModel(
            amplitude=2.7e-14 * u.Unit("cm-2 s-1 TeV-1"),
            index=1.2,
            lambda_=1 / 24 * u.Unit("TeV-1"),
            reference=18 * u.TeV,
        ),
    },
    "HAWC J1825-134": {
        "position": SkyCoord(276.44, -13.42, unit="deg", frame="icrs"),
        "spectral_model": PowerLawSpectralModel(
            index=2.28,
            amplitude="4.2e-15 TeV-1 cm-2 s-1",
            reference=18 * u.TeV,
        ),
    },
}


def make_catalog():
    """Create the HAWC 2021 source catalog."""
    source_names = []
    ra = []
    dec = []
    spectral_models = []

    for source_name, source_data in CATALOG.items():
        source_names.append(source_name)

        position = source_data["position"]
        ra.append(position.ra.deg)
        dec.append(position.dec.deg)

        model = source_data["spectral_model"]
        spectral_models.append(model.tag[1])

    table = Table(
        [source_names, ra, dec, spectral_models],
        names=("source_name", "ra", "dec", "spec_type"),
    )

    table.meta["catalog_name"] = TAG
    table.meta["SED_TYPE"] = SED_TYPE
    table.meta["reference"] = REFERENCE

    return table


def write_catalog(filename=CATALOG_FILE):
    """Write the HAWC 2021 source catalog."""
    table = make_catalog()
    table.write(
        filename,
        format="ascii.ecsv",
        overwrite=True,
    )


if __name__ == "__main__":
    write_catalog()
