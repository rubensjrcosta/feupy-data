#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Create the eHWC source catalog table.

The eHWC catalog is based on:
"Multiple Galactic Sources with Emission Above 56 TeV Detected by HAWC"
https://doi.org/10.1103/PhysRevLett.124.021102

This script writes the main source catalog to ``catalog.ecsv``.
Flux points, models, light curves, or other derived products should be
written by separate scripts and stored in dedicated subdirectories.
"""

import numpy as np
import astropy.units as u

from astropy.table import Table, Column


CATALOG_NAME = "eHWC"
REFERENCE = "https://doi.org/10.1103/PhysRevLett.124.021102"
BIBCODE = "2020PhRvL.124b1102A"
SED_TYPE = "e2dnde"
OUTPUT_FILENAME = "catalog.ecsv"


DATA = {
    "eHWC J0534+220": {
        "ra": 83.61 * u.deg,
        "ra_err": 0.02 * u.deg,
        "dec": 22.00 * u.deg,
        "dec_err": 0.03 * u.deg,
        "spec_type": "ecpl",
        "extension_56TeV": np.nan * u.deg,
        "flux_56TeV": 1.2e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.2e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 12.0,
        "sqrt_TS_100TeV": 4.44,
        "nearest_2hwc_source": "J0534+220",
        "distance_to_2hwc": 0.02 * u.deg,
    },
    "eHWC J1909-193": {
        "ra": 272.46 * u.deg,
        "ra_err": 0.13 * u.deg,
        "dec": -19.34 * u.deg,
        "dec_err": 0.14 * u.deg,
        "spec_type": "ecpl",
        "extension_56TeV": 0.34 * u.deg,
        "flux_56TeV": 2.4e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.5e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 6.97,
        "sqrt_TS_100TeV": 4.82,
        "nearest_2hwc_source": "J1809-190",
        "distance_to_2hwc": 0.03 * u.deg,
    },
    "eHWC J1825-134": {
        "ra": 276.40 * u.deg,
        "ra_err": 0.06 * u.deg,
        "dec": -13.37 * u.deg,
        "dec_err": 0.10 * u.deg,
        "spec_type": "ecpl",
        "extension_56TeV": 0.35 * u.deg,
        "flux_56TeV": 4.6e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.5e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 7.33,
        "sqrt_TS_100TeV": 7.30,
        "nearest_2hwc_source": "J1825-134",
        "distance_to_2hwc": 0.07 * u.deg,
    },
    "eHWC J1839-057": {
        "ra": 279.77 * u.deg,
        "ra_err": 0.12 * u.deg,
        "dec": -5.71 * u.deg,
        "dec_err": 0.11 * u.deg,
        "spec_type": "ecpl",
        "extension_56TeV": 0.34 * u.deg,
        "flux_56TeV": 1.5e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.3e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 7.03,
        "sqrt_TS_100TeV": 6.06,
        "nearest_2hwc_source": "J1837-065",
        "distance_to_2hwc": 0.96 * u.deg,
    },
    "eHWC J1842-035": {
        "ra": 280.72 * u.deg,
        "ra_err": 0.15 * u.deg,
        "dec": -3.15 * u.deg,
        "dec_err": 0.15 * u.deg,
        "spec_type": "ecpl",
        "extension_56TeV": 0.31 * u.deg,
        "flux_56TeV": 1.1e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.3e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 6.63,
        "sqrt_TS_100TeV": 2.70,
        "nearest_2hwc_source": "J1849-001",
        "distance_to_2hwc": 0.44 * u.deg,
    },
    "eHWC J1850+001": {
        "ra": 282.59 * u.deg,
        "ra_err": 0.21 * u.deg,
        "dec": 0.14 * u.deg,
        "dec_err": 0.12 * u.deg,
        "spec_type": "ecpl",
        "extension_56TeV": 0.37 * u.deg,
        "flux_56TeV": 1.3e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.2e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 6.63,
        "sqrt_TS_100TeV": 3.04,
        "nearest_2hwc_source": "J1849-001",
        "distance_to_2hwc": 0.20 * u.deg,
    },
    "eHWC J1907+063": {
        "ra": 286.91 * u.deg,
        "ra_err": 0.10 * u.deg,
        "dec": 6.30 * u.deg,
        "dec_err": 0.12 * u.deg,
        "spec_type": "lp",
        "extension_56TeV": 0.52 * u.deg,
        "flux_56TeV": 2.8e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.4e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 8.04,
        "sqrt_TS_100TeV": 7.30,
        "nearest_2hwc_source": "J1908+063",
        "distance_to_2hwc": 0.16 * u.deg,
    },
    "eHWC J2019+368": {
        "ra": 304.95 * u.deg,
        "ra_err": 0.07 * u.deg,
        "dec": 36.36 * u.deg,
        "dec_err": 0.08 * u.deg,
        "spec_type": "ecpl",
        "extension_56TeV": 0.38 * u.deg,
        "flux_56TeV": 3.6e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.4e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 9.63,
        "sqrt_TS_100TeV": 4.85,
        "nearest_2hwc_source": "J2019+367",
        "distance_to_2hwc": 0.02 * u.deg,
    },
    "eHWC J2030+412": {
        "ra": 307.74 * u.deg,
        "ra_err": 0.09 * u.deg,
        "dec": 41.23 * u.deg,
        "dec_err": 0.07 * u.deg,
        "spec_type": "ecpl",
        "extension_56TeV": 0.18 * u.deg,
        "flux_56TeV": 0.9e-14 * u.Unit("cm-2 s-1"),
        "flux_56TeV_err": 0.2e-14 * u.Unit("cm-2 s-1"),
        "sqrt_TS_56TeV": 6.43,
        "sqrt_TS_100TeV": 3.07,
        "nearest_2hwc_source": "J2031+415",
        "distance_to_2hwc": 0.34 * u.deg,
    },
}


def make_column(data, description, unit=None, fmt=None):
    """Create an Astropy table column with common metadata."""
    return Column(data=data, description=description, unit=unit, format=fmt)


def get_values(data, source_names, key):
    """Return values for one key preserving source order."""
    return [data[name][key] for name in source_names]


def make_ehwc_table(data):
    """Create the eHWC catalog table."""
    source_names = list(data)

    table = Table()
    table.meta["catalog_name"] = CATALOG_NAME
    table.meta["reference"] = REFERENCE
    table.meta["bibcode"] = BIBCODE
    table.meta["SED_TYPE"] = SED_TYPE
    table.meta["comments"] = [
        "eHWC catalog from HAWC sources detected above 56 TeV.",
        f"Reference: {REFERENCE}",
    ]

    table["source_name"] = make_column(
        source_names,
        description="Source name",
    )
    table["ra"] = make_column(
        get_values(data, source_names, "ra"),
        description="Right Ascension (J2000)",
        unit="deg",
        fmt=".3f",
    )
    table["ra_err"] = make_column(
        get_values(data, source_names, "ra_err"),
        description="Statistical uncertainty on right ascension",
        unit="deg",
        fmt=".3f",
    )
    table["dec"] = make_column(
        get_values(data, source_names, "dec"),
        description="Declination (J2000)",
        unit="deg",
        fmt=".3f",
    )
    table["dec_err"] = make_column(
        get_values(data, source_names, "dec_err"),
        description="Statistical uncertainty on declination",
        unit="deg",
        fmt=".3f",
    )
    table["spec_type"] = make_column(
        get_values(data, source_names, "spec_type"),
        description="Spectral model type",
    )
    table["extension_56TeV"] = make_column(
        get_values(data, source_names, "extension_56TeV"),
        description="Source extension above 56 TeV; NaN means point-like source",
        unit="deg",
        fmt=".3f",
    )
    table["flux_56TeV"] = make_column(
        get_values(data, source_names, "flux_56TeV"),
        description="Integral flux above 56 TeV",
        unit="cm-2 s-1",
        fmt=".3e",
    )
    table["flux_56TeV_err"] = make_column(
        get_values(data, source_names, "flux_56TeV_err"),
        description="Statistical uncertainty on flux_56TeV",
        unit="cm-2 s-1",
        fmt=".3e",
    )
    table["sqrt_TS_56TeV"] = make_column(
        get_values(data, source_names, "sqrt_TS_56TeV"),
        description="Square root of TS above 56 TeV",
        fmt=".2f",
    )
    table["sqrt_TS_100TeV"] = make_column(
        get_values(data, source_names, "sqrt_TS_100TeV"),
        description="Square root of TS above 100 TeV",
        fmt=".2f",
    )
    table["nearest_2hwc_source"] = make_column(
        get_values(data, source_names, "nearest_2hwc_source"),
        description="Nearest 2HWC source",
    )
    table["distance_to_2hwc"] = make_column(
        get_values(data, source_names, "distance_to_2hwc"),
        description="Angular distance to nearest 2HWC source",
        unit="deg",
        fmt=".3f",
    )

    return table


def make_ehwc(filename=OUTPUT_FILENAME):
    """Write the eHWC catalog table."""
    table = make_ehwc_table(DATA)

    print(f"Writing {filename}")
    table.write(filename, format="ascii.ecsv", overwrite=True)

    return table


if __name__ == "__main__":
    make_ehwc()
