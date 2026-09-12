# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Fit LogParabola amplitudes for selected LHAASO sources."""

from pathlib import Path

import astropy.units as u
import numpy as np
from astropy.table import Table
from gammapy.datasets import Datasets, FluxPointsDataset
from gammapy.estimators import FluxPoints
from gammapy.modeling import Fit
from gammapy.modeling.models import LogParabolaSpectralModel, SkyModel

REFERENCE = 10 * u.TeV
SED_TYPE = "e2dnde"

BASE_DIR = Path(__file__).resolve().parent
DATASETS_FILE = BASE_DIR / "datasets.yaml"
MODELS_FILE = BASE_DIR / "models.yaml"

DATA_FILES = {
    "LHAASO J1825-1326": {
        "filename": BASE_DIR / "J1825_KM2A_201209.dat",
        "alpha": 0.92,
        "beta": 1.19,
    },
    "LHAASO J1908+0621": {
        "filename": BASE_DIR / "J1908_KM2A_201209.dat",
        "alpha": 2.27,
        "beta": 0.46,
    },
    "LHAASO J2226+6057": {
        "filename": BASE_DIR / "J2228_KM2A_201209.dat",
        "alpha": 1.56,
        "beta": 0.88,
    },
}


def read_lhaaso_dat(filename):
    """Read a LHAASO spectral data file."""
    filename = Path(filename)

    with filename.open() as file:
        values = np.asarray(file.read().split(), dtype=float)

    if values.size % 6 != 0:
        raise ValueError(
            f"Expected a multiple of 6 values in {filename}, found {values.size}"
        )

    values = values.reshape(-1, 6)

    table = Table()

    table["e_ref"] = (values[:, 0] / 1e12) * u.TeV
    table["e2dnde"] = values[:, 1] * u.Unit("erg cm-2 s-1")
    table["e2dnde_errp"] = values[:, 2] * u.Unit("erg cm-2 s-1")
    table["e2dnde_errn"] = values[:, 3] * u.Unit("erg cm-2 s-1")
    table["e_min"] = (values[:, 4] / 1e12) * u.TeV
    table["e_max"] = (values[:, 5] / 1e12) * u.TeV

    table.meta["SED_TYPE"] = SED_TYPE

    return table


def fit_logparabola_amplitude(source_name, config):
    """Fit the LogParabola amplitude for one LHAASO source."""
    table = read_lhaaso_dat(config["filename"])

    flux_points = FluxPoints.from_table(
        table,
        sed_type=SED_TYPE,
    )

    spectral_model = LogParabolaSpectralModel(
        amplitude=1e-12 * u.Unit("cm-2 s-1 TeV-1"),
        reference=REFERENCE,
        alpha=config["alpha"],
        beta=config["beta"],
    )

    spectral_model.alpha.frozen = True
    spectral_model.beta.frozen = True
    spectral_model.reference.frozen = True

    model = SkyModel(
        spectral_model=spectral_model,
        name=source_name,
        datasets_names=[source_name],
    )

    dataset = FluxPointsDataset(
        data=flux_points,
        models=model,
        name=source_name,
    )

    fit = Fit()
    result = fit.run([dataset])

    print("=" * 60)
    print(source_name)
    print("=" * 60)
    print(result)
    print()
    print("Best-fit parameters")
    print(dataset.models.parameters.to_table())
    print()
    print(f"Amplitude = {spectral_model.amplitude.quantity:.3e}")
    print()

    return dataset


def make_datasets():
    """Create fitted datasets for the selected LHAASO sources."""
    datasets = Datasets()

    for source_name, config in DATA_FILES.items():
        dataset = fit_logparabola_amplitude(source_name, config)
        datasets.append(dataset)

    return datasets


def write_datasets(
    filename=DATASETS_FILE,
    filename_models=MODELS_FILE,
):
    """Fit all sources and write the datasets and models."""
    datasets = make_datasets()

    print(f"Writing {filename}")
    print(f"Writing {filename_models}")

    datasets.write(
        filename=filename,
        filename_models=filename_models,
        overwrite=True,
    )


if __name__ == "__main__":
    write_datasets()
