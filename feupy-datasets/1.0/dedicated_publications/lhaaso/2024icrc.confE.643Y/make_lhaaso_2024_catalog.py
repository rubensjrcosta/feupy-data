from pathlib import Path

from astropy import units as u
from astropy.table import Table
from feupy.catalogs.utils import catalog_1lhaaso

BASE_DIR = Path(__file__).resolve().parent

BIBCODE = "2024icrc.confE.643Y"
TAG = "lhaaso-2024icrc"
REFERENCE = "https://doi.org/10.22323/1.444.0643"

CATALOG_FILE = BASE_DIR / "lhaaso_2024_catalog.ecsv"

SOURCES = (
    "1LHAASO J1825-1256u",
    "1LHAASO J1825-1337u",
    "1LHAASO J1825-1418",
)


def make_catalog():
    """Create the LHAASO 2024 dedicated-publication catalog."""
    source_names = []
    ra = []
    dec = []

    for source_name in SOURCES:
        source = catalog_1lhaaso[source_name]

        source_names.append(source_name)
        ra.append(source.position.ra.deg)
        dec.append(source.position.dec.deg)

    table = Table(
        [source_names, ra, dec],
        names=("source_name", "ra", "dec"),
    )

    table["source_name"].description = "Source name"
    table["ra"].unit = u.deg
    table["dec"].unit = u.deg

    table.meta["catalog_name"] = TAG
    table.meta["bibcode"] = BIBCODE
    table.meta["reference"] = REFERENCE

    return table


def write_catalog():
    """Write the catalog to ECSV."""
    catalog = make_catalog()
    catalog.write(
        CATALOG_FILE,
        format="ascii.ecsv",
        overwrite=True,
    )


if __name__ == "__main__":
    write_catalog()
