# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Generate the eHWC source catalog.

The eHWC source catalog is based on:

Multiple Galactic Sources with Emission Above 56 TeV Detected by HAWC
https://doi.org/10.1103/PhysRevLett.124.021102
"""

from pathlib import Path

import astropy.units as u
import numpy as np
from astropy.table import Column, Table
from feupy.utils.formatting import string_to_filename
from feupy.utils.tables.utils import pad_list_to_length

REFERENCE = "https://doi.org/10.1103/PhysRevLett.124.021102"
SED_TYPE = "e2dnde"

BASE_DIR = Path(__file__).resolve().parent
FLUX_POINTS_DIR = BASE_DIR / "flux-points"
CATALOG_FILE = BASE_DIR / "ehwc_catalog.ecsv"


DATA = {
    "eHWC J0534+220": {
        "ra": 83.61 * u.deg,
        "ra_err": 0.02 * u.deg,
        "dec": 22.00 * u.deg,
        "dec_err": 0.03 * u.deg,
        "spectral_model_type": "ecpl",
        "extension_56TeV": np.nan * u.deg,
        "flux_56TeV": 1.2e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.2e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 12.0,
        "sqrt_TS_100TeV": 4.44,
        "nearest_2HWC_source": "J0534+220",
        "distance_to_2HWC": 0.02 * u.deg,
    },
    "eHWC J1809-193": {
        "ra": 272.46 * u.deg,
        "ra_err": 0.13 * u.deg,
        "dec": -19.34 * u.deg,
        "dec_err": 0.14 * u.deg,
        "spectral_model_type": "ecpl",
        "extension_56TeV": 0.34 * u.deg,
        "flux_56TeV": 2.4e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.5e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 6.97,
        "sqrt_TS_100TeV": 4.82,
        "nearest_2HWC_source": "J1809-190",
        "distance_to_2HWC": 0.03 * u.deg,
    },
    "eHWC J1825-134": {
        "ra": 276.40 * u.deg,
        "ra_err": 0.06 * u.deg,
        "dec": -13.37 * u.deg,
        "dec_err": 0.10 * u.deg,
        "spectral_model_type": "ecpl",
        "extension_56TeV": 0.35 * u.deg,
        "flux_56TeV": 4.6e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.5e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 7.33,
        "sqrt_TS_100TeV": 7.30,
        "nearest_2HWC_source": "J1825-134",
        "distance_to_2HWC": 0.07 * u.deg,
    },
    "eHWC J1839-057": {
        "ra": 279.77 * u.deg,
        "ra_err": 0.12 * u.deg,
        "dec": -5.71 * u.deg,
        "dec_err": 0.11 * u.deg,
        "spectral_model_type": "ecpl",
        "extension_56TeV": 0.34 * u.deg,
        "flux_56TeV": 1.5e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.3e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 7.03,
        "sqrt_TS_100TeV": 6.06,
        "nearest_2HWC_source": "J1837-065",
        "distance_to_2HWC": 0.96 * u.deg,
    },
    "eHWC J1842-035": {
        "ra": 280.72 * u.deg,
        "ra_err": 0.15 * u.deg,
        "dec": -3.15 * u.deg,
        "dec_err": 0.15 * u.deg,
        "spectral_model_type": "ecpl",
        "extension_56TeV": 0.31 * u.deg,
        "flux_56TeV": 1.1e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.3e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 6.63,
        "sqrt_TS_100TeV": 2.70,
        "nearest_2HWC_source": "J1849-001",
        "distance_to_2HWC": 0.44 * u.deg,
    },
    "eHWC J1850+001": {
        "ra": 282.59 * u.deg,
        "ra_err": 0.21 * u.deg,
        "dec": 0.14 * u.deg,
        "dec_err": 0.12 * u.deg,
        "spectral_model_type": "ecpl",
        "extension_56TeV": 0.37 * u.deg,
        "flux_56TeV": 1.3e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.2e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 6.63,
        "sqrt_TS_100TeV": 3.04,
        "nearest_2HWC_source": "J1849-001",
        "distance_to_2HWC": 0.20 * u.deg,
    },
    "eHWC J1907+063": {
        "ra": 286.91 * u.deg,
        "ra_err": 0.10 * u.deg,
        "dec": 6.30 * u.deg,
        "dec_err": 0.12 * u.deg,
        "spectral_model_type": "lp",
        "extension_56TeV": 0.52 * u.deg,
        "flux_56TeV": 2.8e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.4e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 8.04,
        "sqrt_TS_100TeV": 7.30,
        "nearest_2HWC_source": "J1908+063",
        "distance_to_2HWC": 0.16 * u.deg,
    },
    "eHWC J2019+368": {
        "ra": 304.95 * u.deg,
        "ra_err": 0.07 * u.deg,
        "dec": 36.36 * u.deg,
        "dec_err": 0.08 * u.deg,
        "spectral_model_type": "ecpl",
        "extension_56TeV": 0.38 * u.deg,
        "flux_56TeV": 3.6e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.4e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 9.63,
        "sqrt_TS_100TeV": 4.85,
        "nearest_2HWC_source": "J2019+367",
        "distance_to_2HWC": 0.02 * u.deg,
    },
    "eHWC J2030+412": {
        "ra": 307.74 * u.deg,
        "ra_err": 0.09 * u.deg,
        "dec": 41.23 * u.deg,
        "dec_err": 0.07 * u.deg,
        "spectral_model_type": "ecpl",
        "extension_56TeV": 0.18 * u.deg,
        "flux_56TeV": 0.9e-14 * u.ph / (u.cm**2 * u.s),
        "flux_56TeV_err": 0.2e-14 * u.ph / (u.cm**2 * u.s),
        "sqrt_TS_56TeV": 6.43,
        "sqrt_TS_100TeV": 3.07,
        "nearest_2HWC_source": "J2031+415",
        "distance_to_2HWC": 0.34 * u.deg,
    },
}


def make_catalog_table():
    """Create the eHWC catalog table."""
    source_names = list(DATA)

    table = Table()

    table["source_name"] = source_names
    table["ra"] = [DATA[name]["ra"] for name in source_names]
    table["ra_err"] = [DATA[name]["ra_err"] for name in source_names]
    table["dec"] = [DATA[name]["dec"] for name in source_names]
    table["dec_err"] = [DATA[name]["dec_err"] for name in source_names]

    table["spec_type"] = [DATA[name]["spectral_model_type"] for name in source_names]

    table["extension_56TeV"] = [DATA[name]["extension_56TeV"] for name in source_names]

    table["Flux_56TeV"] = [DATA[name]["flux_56TeV"] for name in source_names]
    table["Flux_56TeV_err"] = [DATA[name]["flux_56TeV_err"] for name in source_names]

    table["sqrt_TS_56TeV"] = [DATA[name]["sqrt_TS_56TeV"] for name in source_names]
    table["sqrt_TS_100TeV"] = [DATA[name]["sqrt_TS_100TeV"] for name in source_names]

    table["nearest_2HWC_source"] = [
        DATA[name]["nearest_2HWC_source"] for name in source_names
    ]
    table["distance_to_2HWC"] = [
        DATA[name]["distance_to_2HWC"] for name in source_names
    ]

    table["Flux_56TeV"].format = ".3e"
    table["Flux_56TeV_err"].format = ".3e"

    table.meta["catalog_name"] = "eHWC"
    table.meta["SED_TYPE"] = SED_TYPE
    table.meta["comments"] = [f"reference: {REFERENCE}"]

    add_flux_points(table)

    return table


def add_flux_points(table):
    """Add published eHWC flux points to the catalog table."""
    source_names = list(table["source_name"])

    sed_e_ref = []
    sed_e2dnde = []
    sed_e2dnde_errp = []
    sed_e2dnde_errn = []
    sed_e2dnde_ul = []
    sed_is_ul = []

    nan_values = pad_list_to_length(10, [])

    for source_name in source_names:
        filename = FLUX_POINTS_DIR / f"{string_to_filename(source_name)}.ecsv"

        if filename.exists():
            flux_table = Table.read(filename, format="ascii.ecsv")

            sed_e_ref.append(flux_table["e_ref"])
            sed_e2dnde.append(flux_table["e2dnde"])
            sed_e2dnde_errp.append(flux_table["e2dnde_errp"])
            sed_e2dnde_errn.append(flux_table["e2dnde_errn"])
            sed_e2dnde_ul.append(flux_table["e2dnde_ul"])
            sed_is_ul.append(flux_table["is_ul"])
        else:
            sed_e_ref.append(nan_values)
            sed_e2dnde.append(nan_values)
            sed_e2dnde_errp.append(nan_values)
            sed_e2dnde_errn.append(nan_values)
            sed_e2dnde_ul.append(nan_values)
            sed_is_ul.append(nan_values)

    table["sed_e_ref"] = Column(
        data=sed_e_ref,
        unit="TeV",
        description="Reference energy",
        format=".3f",
    )

    table["sed_e2dnde"] = Column(
        data=sed_e2dnde,
        unit="TeV cm-2 s-1",
        description="SED value",
        format=".3e",
    )

    table["sed_e2dnde_errp"] = Column(
        data=sed_e2dnde_errp,
        unit="TeV cm-2 s-1",
        description="SED positive error",
        format=".3e",
    )

    table["sed_e2dnde_errn"] = Column(
        data=sed_e2dnde_errn,
        unit="TeV cm-2 s-1",
        description="SED negative error",
        format=".3e",
    )

    table["sed_e2dnde_ul"] = Column(
        data=sed_e2dnde_ul,
        unit="TeV cm-2 s-1",
        description="SED upper limit",
        format=".3e",
    )

    table["sed_is_ul"] = Column(
        data=sed_is_ul,
        description="SED upper limit flag",
    )


def write_catalog(filename=CATALOG_FILE):
    """Write the eHWC catalog."""
    filename = Path(filename)

    table = make_catalog_table()

    print(f"Writing {filename}")
    table.write(filename, format="ascii.ecsv", overwrite=True)


if __name__ == "__main__":
    write_catalog()
