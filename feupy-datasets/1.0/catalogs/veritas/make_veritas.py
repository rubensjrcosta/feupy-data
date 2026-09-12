# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Create VERITAS catalog files for FeuPy.

Outputs
-------
- veritas_catalog.ecsv
- datasets.yaml
- models.yaml
- models_covariance.dat
- VER_*.fits
"""

from pathlib import Path

import astropy.units as u
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.table import Column, Table
from gammapy.datasets import Datasets, FluxPointsDataset
from gammapy.estimators import FluxPoints
from gammapy.modeling import Fit
from gammapy.modeling.models import PowerLawSpectralModel, SkyModel

REFERENCE = "https://iopscience.iop.org/article/10.3847/1538-4357/aac4a2"
SED_TYPE = "dnde"
DNDE_UNIT = u.Unit("GeV-1 cm-2 s-1")
DATA_NAME = "VERITAS"

DATA = {
    "VER J2031+415": {
        "position": SkyCoord(l=80.25, b=1.20, unit="deg", frame="galactic"),
        "spectral_model": "pl",
        "reference_energy": "2300 GeV",
        "flux_points": [
            (422, 750, 3.26e-15, 1.57e-15, np.nan, False),
            (750, 1330, 6.85e-16, 2.73e-16, np.nan, False),
            (1330, 2370, 1.97e-16, 8.26e-17, np.nan, False),
            (2370, 4220, 3.95e-17, 2.75e-17, np.nan, False),
            (4220, 7500, 3.62e-17, 1.24e-17, np.nan, False),
            (7500, 13300, 6.92e-18, np.nan, 6.92e-18, True),
            (13300, 23700, 1.26e-18, 1.38e-18, np.nan, False),
            (23700, 42200, 5.99e-19, 4.55e-19, np.nan, False),
        ],
    },
    "VER J2019+407": {
        "position": SkyCoord(l=78.30, b=2.55, unit="deg", frame="galactic"),
        "spectral_model": "pl",
        "reference_energy": "1500 GeV",
        "flux_points": [
            (750, 1330, 1.56e-15, 4.17e-16, np.nan, False),
            (1330, 2370, 3.91e-16, 1.09e-16, np.nan, False),
            (2370, 4220, 2.65e-17, 3.03e-17, np.nan, False),
            (4220, 7500, 2.73e-17, 1.27e-17, np.nan, False),
        ],
    },
    "VER J2019+368": {
        "position": SkyCoord(l=74.97, b=0.35, unit="deg", frame="galactic"),
        "spectral_model": "pl",
        "reference_energy": "3110 GeV",
        "flux_points": [
            (422, 750, 1.62e-15, 1.68e-15, np.nan, False),
            (750, 1330, 6.68e-16, 2.34e-16, np.nan, False),
            (1330, 2370, 3.31e-16, 7.2e-17, np.nan, False),
            (2370, 4220, 1.47e-16, 2.64e-17, np.nan, False),
            (4220, 7500, 4.29e-17, 1.09e-17, np.nan, False),
            (7500, 13300, 8.01e-18, 3.59e-18, np.nan, False),
            (13300, 23700, 3.3e-18, 1.6e-18, np.nan, False),
            (23700, 42200, 5.37e-19, 3.99e-19, np.nan, False),
        ],
    },
    "VER J2018+367*": {
        "position": SkyCoord(l=74.87, b=0.42, unit="deg", frame="galactic"),
        "spectral_model": "pl",
        "reference_energy": "2710 GeV",
        "flux_points": [
            (750, 1330, 2.98e-16, 1.35e-16, np.nan, False),
            (1330, 2370, 1.5e-16, 4.41e-17, np.nan, False),
            (2370, 4220, 5.12e-17, 1.63e-17, np.nan, False),
            (4220, 7500, 6.74e-18, 5.12e-18, np.nan, False),
            (7500, 13300, 3.1e-18, 2.44e-18, np.nan, False),
            (13300, 23700, 1.6e-18, 9.33e-19, np.nan, False),
        ],
    },
    "VER J2020+368*": {
        "position": SkyCoord(l=74.13, b=0.19, unit="deg", frame="galactic"),
        "spectral_model": "pl",
        "reference_energy": "3270 GeV",
        "flux_points": [
            (750, 1330, 2.16e-16, 1.09e-16, np.nan, False),
            (1330, 2370, 9.96e-17, 3.48e-17, np.nan, False),
            (2370, 4220, 3.95e-17, 1.43e-17, np.nan, False),
            (4220, 7500, 4.34e-18, 4.55e-18, np.nan, False),
            (7500, 13300, 8.03e-18, 3.22e-18, np.nan, False),
            (13300, 23700, 2.29e-18, 1.27e-18, np.nan, False),
        ],
    },
    "VER J2016+371": {
        "position": SkyCoord(l=74.94, b=1.16, unit="deg", frame="galactic"),
        "spectral_model": "pl",
        "reference_energy": "2510 GeV",
        "flux_points": [
            (681, 1470, 2.13e-16, 1.85e-16, np.nan, False),
            (1470, 3160, 3.96e-17, 2.53e-17, np.nan, False),
            (3160, 6810, 4.95e-18, 6.48e-18, np.nan, False),
            (6810, 14700, 2.55e-18, 2.36e-18, np.nan, False),
        ],
    },
}


def make_flux_points_table(source_name, source_data):
    """Create a flux-points table for one VERITAS source."""
    rows = source_data["flux_points"]

    table = Table()
    table["e_min"] = [row[0] for row in rows] * u.GeV
    table["e_max"] = [row[1] for row in rows] * u.GeV
    table["dnde"] = [row[2] for row in rows] * DNDE_UNIT
    table["dnde_err"] = [row[3] for row in rows] * DNDE_UNIT
    table["dnde_ul"] = [row[4] for row in rows] * DNDE_UNIT
    table["is_ul"] = [row[5] for row in rows]

    table["e_min"].description = "Energy bin lower edge"
    table["e_max"].description = "Energy bin upper edge"
    table["dnde"].description = "Differential photon flux"
    table["dnde_err"].description = "Symmetric 1-sigma error on dnde"
    table["dnde_ul"].description = "Upper limit on dnde"
    table["is_ul"].description = "Boolean flag for upper limits"

    table.meta["source_name"] = source_name
    table.meta["SED_TYPE"] = SED_TYPE
    table.meta["reference"] = REFERENCE

    return table


def make_initial_spectral_model(source_data):
    """Create the initial spectral model used for the fit."""
    return PowerLawSpectralModel(
        index=1.8,
        amplitude="2e-12 cm-2 s-1 TeV-1",
        reference=source_data["reference_energy"],
    )


def fit_sky_model(source_name, flux_points, source_data):
    """Fit a power-law sky model to flux points."""
    model = SkyModel(
        spectral_model=make_initial_spectral_model(source_data),
        name=source_name,
    )

    dataset = FluxPointsDataset(data=flux_points, name=source_name)
    datasets = Datasets([dataset])
    datasets.models = [model]

    Fit().run(datasets=datasets)

    return SkyModel(
        spectral_model=model.spectral_model,
        name=source_name,
        datasets_names=[source_name],
    )


def make_dataset(source_name, source_data):
    """Create one VERITAS flux-points dataset."""
    table = make_flux_points_table(source_name, source_data)
    flux_points = FluxPoints.from_table(table, sed_type=SED_TYPE)
    model = fit_sky_model(source_name, flux_points, source_data)

    return FluxPointsDataset(
        data=flux_points,
        models=[model],
        name=source_name,
    )


def make_datasets(data):
    """Create all VERITAS datasets."""
    datasets = Datasets()

    for source_name, source_data in data.items():
        datasets.append(make_dataset(source_name, source_data))

    return datasets


def make_catalog_table(data):
    """Create the VERITAS source catalog table."""
    names = list(data)

    table = Table()
    table.meta["catalog_name"] = DATA_NAME
    table.meta["SED_TYPE"] = SED_TYPE
    table.meta["reference"] = REFERENCE

    table["source_name"] = names
    table["source_name"].description = "Source name"

    table["ra"] = Column(
        data=np.full(len(names), np.nan),
        description="Right Ascension (J2000)",
        unit="deg",
        format=".3f",
    )
    table["dec"] = Column(
        data=np.full(len(names), np.nan),
        description="Declination (J2000)",
        unit="deg",
        format=".3f",
    )
    table["spectral_model"] = Column(
        data=[data[name]["spectral_model"] for name in names],
        description="Spectral model type",
    )

    for index, name in enumerate(names):
        position = data[name]["position"].icrs
        table["ra"][index] = position.ra.deg
        table["dec"][index] = position.dec.deg

    return table


def write_outputs(data, output_dir="."):
    """Write VERITAS catalog, datasets, and models."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    datasets = make_datasets(data)
    datasets.write(
        filename=output_dir / "datasets.yaml",
        filename_models=output_dir / "models.yaml",
        overwrite=True,
    )

    catalog = make_catalog_table(data)
    catalog.write(
        output_dir / "veritas_catalog.ecsv",
        format="ascii.ecsv",
        overwrite=True,
    )


if __name__ == "__main__":
    write_outputs(DATA)
