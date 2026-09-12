# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Generate the H.E.S.S. 2019 dedicated-publication catalog."""

from pathlib import Path

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table

BIBCODE = "2019A&A...621A.116H"
TAG = "hess-2019A&A"
SED_TYPE = "e2dnde"
REFERENCE = "https://doi.org/10.1051/0004-6361/201834335"

BASE_DIR = Path(__file__).resolve().parent
CATALOG_FILE = BASE_DIR / "hess_2019_catalog.ecsv"

CATALOG = {
    "HESS J1825-137": {
        "position": SkyCoord(
            "18 25 49 -13 46 35",
            unit=(u.hourangle, u.deg),
        ),
        "radius": 0.8 * u.deg,
        "radius_core": 0.4 * u.deg,
        "spec_type": "ecpl",
    },
}


def format_table(table):
    """Set display formats for catalog columns."""
    for column in table.colnames:
        if column.startswith(("Flux", "sed_dnde")):
            table[column].format = ".3e"
        elif column.startswith(
            (
                "ra",
                "dec",
                "e_min",
                "e_max",
                "e_ref",
                "sed_e",
                "sqrt_ts",
                "norm",
                "ts",
                "stat",
            )
        ):
            table[column].format = ".3f"

    return table


def make_catalog():
    """Create the H.E.S.S. 2019 source catalog."""
    source_names = []
    ra = []
    dec = []
    radius = []
    radius_core = []
    spectral_types = []

    for source_name, source_data in CATALOG.items():
        source_names.append(source_name)
        ra.append(source_data["position"].ra.deg)
        dec.append(source_data["position"].dec.deg)
        radius.append(source_data["radius"])
        radius_core.append(source_data["radius_core"])
        spectral_types.append(source_data["spec_type"])

    table = Table(
        [
            source_names,
            ra,
            dec,
            radius,
            radius_core,
            spectral_types,
        ],
        names=(
            "source_name",
            "ra",
            "dec",
            "radius",
            "radius_core",
            "spec_type",
        ),
    )

    table.meta["catalog_name"] = TAG
    table.meta["SED_TYPE"] = SED_TYPE
    table.meta["reference"] = REFERENCE

    table["ra"].unit = "deg"
    table["dec"].unit = "deg"

    return format_table(table)


def write_catalog(filename=CATALOG_FILE):
    """Write the H.E.S.S. 2019 source catalog."""
    table = make_catalog()
    table.write(
        filename,
        format="ascii.ecsv",
        overwrite=True,
    )


if __name__ == "__main__":
    write_catalog()
