# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Generate the ATNF Pulsar Catalogue used by FeuPy."""

import logging
from pathlib import Path

import numpy as np
from psrqpy import QueryATNF

log = logging.getLogger(__name__)

CATALOG_NAME = "psrcat"
CATALOG_FILE = Path(__file__).resolve().parent / "psrcat_catalog.fits"

PSR_PARAMS = [
    "JNAME",
    "RAJD",
    "DECJD",
    "DIST",
    "DIST_DM",
    "AGE",
    "P0",
    "BSURF",
    "EDOT",
    "TYPE",
    "ASSOC",
]


def format_table(table):
    """Set display formats for catalog columns."""
    for column in table.colnames:
        if column.startswith(("DEJ", "RAJ", "DIST")):
            table[column].format = ".3f"
        elif column.startswith(("AGE", "EDOT", "BSURF", "P0")):
            table[column].format = ".2e"

    return table


def clean_string_column(table, name):
    """Convert a column to a FITS-compatible string column."""
    values = [
        "" if value is None or str(value) == "--" else str(value)
        for value in table[name]
    ]

    max_length = max(len(value) for value in values)
    table[name] = np.asarray(values, dtype=f"<U{max_length}")


def make_catalog():
    """Query and prepare the ATNF Pulsar Catalogue."""
    log.info("Querying the ATNF Pulsar Catalogue...")
    table = QueryATNF(params=PSR_PARAMS).table

    clean_string_column(table, "TYPE")
    clean_string_column(table, "ASSOC")

    names = [f"PSR {jname}" for jname in table["JNAME"]]
    max_length = max(len(name) for name in names)
    table["NAME"] = np.asarray(names, dtype=f"<U{max_length}")

    table.rename_columns(
        ["RAJD", "DECJD"],
        ["RAJ2000", "DEJ2000"],
    )
    table.rename_columns(
        ["RAJD_ERR", "DECJD_ERR"],
        ["RAJ2000_ERR", "DEJ2000_ERR"],
    )

    table.meta["catalog_name"] = CATALOG_NAME

    table = table[
        "NAME",
        "JNAME",
        "DEJ2000",
        "DEJ2000_ERR",
        "RAJ2000",
        "RAJ2000_ERR",
        "DIST",
        "DIST_DM",
        "AGE",
        "EDOT",
        "BSURF",
        "P0",
        "P0_ERR",
        "ASSOC",
        "TYPE",
    ]

    return format_table(table)


def write_catalog(filename=CATALOG_FILE):
    """Write the ATNF Pulsar Catalogue to FITS."""
    filename = Path(filename)
    table = make_catalog()

    log.info("Writing catalog to %s...", filename)
    table.write(
        filename,
        format="fits",
        overwrite=True,
    )
    log.info("Catalog successfully written.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    write_catalog()
