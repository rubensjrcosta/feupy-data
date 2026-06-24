#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Make eHWC flux-points tables.

The eHWC flux points are from:

Multiple Galactic Sources with Emission Above 56 TeV Detected by HAWC
https://doi.org/10.1103/PhysRevLett.124.021102
"""

import numpy as np
import astropy.units as u

from astropy.table import Table
from gammapy.estimators import FluxPoints
from gammapy.utils.scripts import make_path
from feupy.utils.formatting import string_to_filename
    

ENERGY_UNIT = u.TeV
SED_UNIT = u.Unit("TeV cm-2 s-1")

E_MIN = np.array([1.00, 1.78, 3.16, 5.62, 10.0, 17.8, 31.6, 56.2, 100.0, 177.0])
E_MAX = np.array([1.78, 3.16, 5.62, 10.0, 17.8, 31.6, 56.2, 100.0, 177.0, 316.0])

REFERENCE = "https://doi.org/10.1103/PhysRevLett.124.021102"
SED_TYPE = "e2dnde"


FLUX_POINTS_DATA = {
    "eHWC J1825-134": {
        "e_ref": [1.34, 1.96, 2.91, 5.20, 9.54, 15.95, 30.44, 58.18, 98.17, 153.5],
        "sqrt_ts": [4.29, 11.3, 12.9, 14.7, 16.0, 20.2, 17.2, 12.6, 5.72, 4.03],
        "e2dnde": [2.41e-11, 2.22e-11, 2.58e-11, 2.24e-11, 1.77e-11,
                   1.63e-11, 1.08e-11, 6.22e-12, 2.59e-12, 3.45e-12],
        "e2dnde_err": [0.56e-11, 0.20e-11, 0.21e-11, 0.17e-11, 0.13e-11,
                       0.11e-11, 0.09e-11, 0.76e-12, 0.68e-12, 1.25e-12],
    },
    "eHWC J1907+063": {
        "e_ref": [1.16, 1.80, 3.13, 5.59, 10.13, 19.0, 34.79, 60.89, 105.4, 180.8],
        "sqrt_ts": [11.7, 12.4, 13.7, 16.2, 16.3, 13.6, 11.4, 7.66, 6.54, 2.66],
        "e2dnde": [1.59e-11, 1.52e-11, 1.51e-11, 1.21e-11, 9.36e-12,
                   6.36e-12, 4.25e-12, 2.78e-12, 2.49e-12, 1.25e-12],
        "e2dnde_err": [0.14e-11, 0.13e-11, 0.11e-11, 0.08e-11, 0.63e-12,
                       0.53e-12, 0.46e-12, 0.46e-12, 0.53e-12, 0.61e-12],
    },
    "eHWC J2019+368": {
        "e_ref": [1.71, 2.69, 4.13, 6.45, 10.84, 19.39, 34.59, 59.16, 102.4, 131.8],
        "sqrt_ts": [3.06, 7.05, 7.11, 11.5, 16.8, 17.6, 10.6, 8.24, 6.31, 0.33],
        "e2dnde": [2.21e-12, 4.11e-12, 3.79e-12, 4.50e-12, 4.74e-12,
                   4.39e-12, 2.29e-12, 1.77e-12, 1.50e-12, np.nan],
        "e2dnde_err": [0.71e-12, 0.61e-12, 0.56e-12, 0.42e-12, 0.34e-12,
                       0.34e-12, 0.29e-12, 0.31e-12, 0.35e-12, np.nan],
        "e2dnde_ul": [np.nan, np.nan, np.nan, np.nan, np.nan,
                      np.nan, np.nan, np.nan, np.nan, 2.74e-13],
    },
}


def make_flux_points_table(source_name, source_data):
    """Create one eHWC flux-points table."""
    e_ref = np.asarray(source_data["e_ref"])
    sqrt_ts = np.asarray(source_data["sqrt_ts"])
    e2dnde = np.asarray(source_data["e2dnde"])
    e2dnde_err = np.asarray(source_data["e2dnde_err"])
    e2dnde_ul = np.asarray(source_data.get("e2dnde_ul", np.full_like(e2dnde, np.nan)))

    table = Table()
    table["e_min"] = E_MIN * ENERGY_UNIT
    table["e_min"].description = "Energy bin lower edge"
    table["e_max"] = E_MAX * ENERGY_UNIT
    table["e_max"].description = "Energy bin upper edge"
    table["e_ref"] = e_ref * ENERGY_UNIT
    table["e_ref"].description = "Reference energy"
    table["sqrt_ts"] = sqrt_ts
    table["sqrt_ts"].description = "Square root of the test statistic"
    table["e2dnde"] = e2dnde * SED_UNIT
    table["e2dnde"].description = "Spectral energy distribution value"
    table["e2dnde_errp"] = e2dnde_err * SED_UNIT
    table["e2dnde_errp"].description = "Positive statistical uncertainty on e2dnde"
    table["e2dnde_errn"] = e2dnde_err * SED_UNIT
    table["e2dnde_errn"].description = "Negative statistical uncertainty on e2dnde"
    table["e2dnde_ul"] = e2dnde_ul * SED_UNIT
    table["e2dnde_ul"].description = "Upper limit on e2dnde"
    table["is_ul"] = np.isfinite(e2dnde_ul)
    table["is_ul"].description = "Upper limit flag"

    table.meta["SED_TYPE"] = SED_TYPE
    table.meta["source_name"] = source_name
    table.meta["reference"] = REFERENCE

    return table


def validate_flux_points_table(table):
    """Validate table with Gammapy."""
    FluxPoints.from_table(table, sed_type=SED_TYPE)


def write_flux_points_tables(outdir="flux-points"):
    """Write all eHWC flux-points tables."""
    outdir = make_path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for source_name, source_data in FLUX_POINTS_DATA.items():
        table = make_flux_points_table(source_name, source_data)
        validate_flux_points_table(table)

        filename = outdir / f"{string_to_filename(source_name)}.ecsv"
        print(f"Writing {filename}")
        table.write(filename, format="ascii.ecsv", overwrite=True)


if __name__ == "__main__":
    write_flux_points_tables()
