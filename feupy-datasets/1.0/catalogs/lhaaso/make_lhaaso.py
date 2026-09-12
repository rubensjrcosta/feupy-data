# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Generate the LHAASO first 12 PeVatrons catalog.

The catalog data are taken from:

Ultrahigh-energy photons up to 1.4 petaelectronvolts from 12 gamma-ray
Galactic sources
https://doi.org/10.1038/s41586-021-03498-z
"""

from pathlib import Path

import astropy.units as u
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.table import Column, Table
from feupy.utils.constants import (
    CU,
    FRAME_ICRS,
    UNIT_DEG,
)
from feupy.utils.sed import (
    DEFAULT_ENERGY_UNIT,
    DEFAULT_SED_UNIT,
)
from feupy.utils.tables.utils import pad_list_to_length
from gammapy.modeling.models import (
    LogParabolaSpectralModel,
    PowerLawSpectralModel,
)

BIBCODE = "2021Natur.594...33C"
TAG = "LHAASO"
REFERENCE = "https://doi.org/10.1038/s41586-021-03498-z"

SED_TYPE = "e2dnde"
DEFAULT_LENGTH = 10
REFERENCE_ENERGY = 100 * u.TeV

BASE_DIR = Path(__file__).resolve().parent
CATALOG_FILE = BASE_DIR / "lhaaso_catalog.ecsv"

DATA_FILES = {
    "LHAASO J1825-1326": BASE_DIR / "J1825_KM2A_201209.dat",
    "LHAASO J1908+0621": BASE_DIR / "J1908_KM2A_201209.dat",
    "LHAASO J2226+6057": BASE_DIR / "J2228_KM2A_201209.dat",
}

CATALOG = {
    "LHAASO J0534+2202": {
        "position": SkyCoord(83.55, 22.05, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 17.8,
        "Energy_max": (0.88, 0.11) * u.PeV,
        "Flux_100TeV": (1.00, 0.14) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=1.00 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J1825-1326": {
        "position": SkyCoord(276.45, -13.45, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 16.4,
        "Energy_max": (0.42, 0.16) * u.PeV,
        "Flux_100TeV": (3.57, 0.52) * CU,
        "spectral_model": LogParabolaSpectralModel(
            alpha=0.92,
            amplitude="1e-12 cm-2 s-1 TeV-1",
            reference=10 * u.TeV,
            beta=1.19,
        ),
    },
    "LHAASO J1839-0545": {
        "position": SkyCoord(279.95, -5.75, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 7.7,
        "Energy_max": (0.21, 0.05) * u.PeV,
        "Flux_100TeV": (0.70, 0.18) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=0.70 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J1843-0338": {
        "position": SkyCoord(280.75, -3.65, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 8.5,
        "Energy_max": (0.26, 0.10) * u.PeV,
        "Flux_100TeV": (0.73, 0.17) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=0.73 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J1849-0003": {
        "position": SkyCoord(282.35, -0.05, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 10.4,
        "Energy_max": (0.35, 0.07) * u.PeV,
        "Flux_100TeV": (0.74, 0.15) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=0.73 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J1908+0621": {
        "position": SkyCoord(287.05, 6.35, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 17.2,
        "Energy_max": (0.44, 0.05) * u.PeV,
        "Flux_100TeV": (1.36, 0.18) * CU,
        "spectral_model": LogParabolaSpectralModel(
            alpha=2.27,
            amplitude="1e-12 cm-2 s-1 TeV-1",
            reference=10 * u.TeV,
            beta=0.46,
        ),
    },
    "LHAASO J1929+1745": {
        "position": SkyCoord(292.25, 17.75, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 7.4,
        "Energy_max": (0.71, 0.07) * u.PeV,
        "Flux_100TeV": (0.38, 0.09) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=0.38 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J1956+2845": {
        "position": SkyCoord(299.05, 28.75, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 7.4,
        "Energy_max": (0.42, 0.03) * u.PeV,
        "Flux_100TeV": (0.41, 0.09) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=0.41 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J2018+3651": {
        "position": SkyCoord(304.75, 36.85, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 10.4,
        "Energy_max": (0.27, 0.02) * u.PeV,
        "Flux_100TeV": (0.50, 0.10) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=0.50 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J2032+4102": {
        "position": SkyCoord(308.05, 41.05, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 10.5,
        "Energy_max": (1.42, 0.13) * u.PeV,
        "Flux_100TeV": (0.54, 0.10) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=0.54 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J2108+5157": {
        "position": SkyCoord(317.15, 51.95, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 8.3,
        "Energy_max": (0.43, 0.05) * u.PeV,
        "Flux_100TeV": (0.38, 0.09) * CU,
        "spectral_model": PowerLawSpectralModel(
            amplitude=0.38 * CU,
            reference=100 * u.TeV,
        ),
    },
    "LHAASO J2226+6057": {
        "position": SkyCoord(336.75, 60.95, unit=UNIT_DEG, frame=FRAME_ICRS),
        "Significance_100TeV": 13.6,
        "Energy_max": (0.57, 0.19) * u.PeV,
        "Flux_100TeV": (1.05, 0.16) * CU,
        "spectral_model": LogParabolaSpectralModel(
            alpha=1.56,
            amplitude="1e-12 cm-2 s-1 TeV-1",
            reference=10 * u.TeV,
            beta=0.88,
        ),
    },
}


def read_sed_data(filename, length=DEFAULT_LENGTH):
    """Read LHAASO spectral energy distribution data."""
    e_ref = []
    e2dnde = []
    e2dnde_errn = []
    e2dnde_errp = []

    with Path(filename).open() as file:
        for line in file:
            values = line.split()

            if len(values) < 2:
                continue

            try:
                energy = float(values[0]) / 1e12
                flux = float(values[1])
                errp = float(values[2]) if len(values) > 2 else flux
                errn = float(values[3]) if len(values) > 3 else errp
            except ValueError:
                continue

            if flux / errn < 1:
                continue

            e_ref.append(energy)
            e2dnde.append(flux)
            e2dnde_errn.append(errn)
            e2dnde_errp.append(errp)

    return (
        pad_list_to_length(length, e_ref),
        pad_list_to_length(length, e2dnde),
        pad_list_to_length(length, e2dnde_errn),
        pad_list_to_length(length, e2dnde_errp),
    )


def make_catalog_table():
    """Create the LHAASO catalog table."""
    rows = []

    for source_name, source_data in CATALOG.items():
        model = source_data["spectral_model"]

        if isinstance(model, PowerLawSpectralModel):
            spec_type = "pl"
        elif isinstance(model, LogParabolaSpectralModel):
            spec_type = "lp"
        else:
            raise TypeError(
                f"Unsupported spectral model for {source_name!r}: "
                f"{type(model).__name__}"
            )

        rows.append(
            (
                source_name,
                source_data["position"].ra.deg,
                source_data["position"].dec.deg,
                source_data["Significance_100TeV"],
                source_data["Energy_max"][0].to_value(u.PeV),
                source_data["Energy_max"][1].to_value(u.PeV),
                source_data["Flux_100TeV"][0].to_value(u.Unit("cm-2 s-1 TeV-1")),
                source_data["Flux_100TeV"][1].to_value(u.Unit("cm-2 s-1 TeV-1")),
                spec_type,
            )
        )

    table = Table(
        rows=rows,
        names=[
            "source_name",
            "ra",
            "dec",
            "Significance_100TeV",
            "Energy_max",
            "Energy_max_error",
            "Flux_100TeV",
            "Flux_error_100TeV",
            "spec_type",
        ],
    )

    table["ra"].unit = u.deg
    table["dec"].unit = u.deg
    table["Energy_max"].unit = u.PeV
    table["Energy_max_error"].unit = u.PeV
    table["Flux_100TeV"].unit = u.Unit("cm-2 s-1 TeV-1")
    table["Flux_error_100TeV"].unit = u.Unit("cm-2 s-1 TeV-1")

    table.meta["catalog_name"] = TAG
    table.meta["SED_TYPE"] = SED_TYPE
    table.meta["reference"] = REFERENCE

    add_sed_columns(table)
    format_table(table)

    return table


def add_sed_columns(table):
    """Add SED information to the catalog table."""
    e_ref_list = []
    e2dnde_list = []
    e2dnde_err_list = []
    e2dnde_errn_list = []
    e2dnde_errp_list = []
    e2dnde_ul_list = []
    is_ul_list = []

    for row in table:
        if row["spec_type"] == "pl":
            e_ref = pad_list_to_length(
                DEFAULT_LENGTH,
                [REFERENCE_ENERGY.to_value(u.TeV)],
            )
            e2dnde = pad_list_to_length(
                DEFAULT_LENGTH,
                [row["Flux_100TeV"] * REFERENCE_ENERGY.to_value(u.TeV) ** 2],
            )
            e2dnde_err = pad_list_to_length(
                DEFAULT_LENGTH,
                [row["Flux_error_100TeV"] * REFERENCE_ENERGY.to_value(u.TeV) ** 2],
            )
            e2dnde_errn = pad_list_to_length(DEFAULT_LENGTH, [])
            e2dnde_errp = pad_list_to_length(DEFAULT_LENGTH, [])
        else:
            filename = DATA_FILES[row["source_name"]]
            e_ref, e2dnde, e2dnde_errn, e2dnde_errp = read_sed_data(filename)
            e2dnde_err = pad_list_to_length(DEFAULT_LENGTH, [])

        e2dnde_ul = pad_list_to_length(DEFAULT_LENGTH, [])
        is_ul = np.full(DEFAULT_LENGTH, None, dtype=bool).tolist()

        e_ref_list.append(e_ref)
        e2dnde_list.append(e2dnde)
        e2dnde_err_list.append(e2dnde_err)
        e2dnde_errn_list.append(e2dnde_errn)
        e2dnde_errp_list.append(e2dnde_errp)
        e2dnde_ul_list.append(e2dnde_ul)
        is_ul_list.append(is_ul)

    table["sed_e_ref"] = Column(
        e_ref_list,
        unit=DEFAULT_ENERGY_UNIT[SED_TYPE],
        description="Reference energy",
    )
    table["sed_e2dnde"] = Column(
        e2dnde_list,
        unit=DEFAULT_SED_UNIT[SED_TYPE],
        description="SED value",
    )
    table["sed_e2dnde_err"] = Column(
        e2dnde_err_list,
        unit=DEFAULT_SED_UNIT[SED_TYPE],
        description="SED error",
    )
    table["sed_e2dnde_errn"] = Column(
        e2dnde_errn_list,
        unit=DEFAULT_SED_UNIT[SED_TYPE],
        description="SED negative error",
    )
    table["sed_e2dnde_errp"] = Column(
        e2dnde_errp_list,
        unit=DEFAULT_SED_UNIT[SED_TYPE],
        description="SED positive error",
    )
    table["sed_e2dnde_ul"] = Column(
        e2dnde_ul_list,
        unit=DEFAULT_SED_UNIT[SED_TYPE],
        description="SED upper limit",
    )

    table["sed_is_ul"] = Column(
        is_ul_list,
        unit=u.Unit(""),
        description="Whether the data point is an upper limit",
    )

    table["spec_reference"] = REFERENCE_ENERGY


def format_table(table):
    """Format catalog columns."""
    for column in table.colnames:
        if column.startswith(("Flux", "sed_e2dnde")):
            table[column].format = ".3e"
        elif column.startswith(("sed_e", "Energy", "Significance")):
            table[column].format = ".3f"


def write_catalog(filename=CATALOG_FILE):
    """Generate and write the LHAASO catalog."""
    filename = Path(filename)
    table = make_catalog_table()

    print(f"Writing {filename}")
    table.write(filename, format="ascii.ecsv", overwrite=True)


if __name__ == "__main__":
    write_catalog()
