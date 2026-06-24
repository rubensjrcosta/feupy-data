"""
Script to build FluxPointsDataset for the three LHAASO sources and fit the LogParabola amplitude
"""

import numpy as np
import astropy.units as u

from astropy.table import Table

from gammapy.estimators import FluxPoints
from gammapy.modeling import Fit
from gammapy.modeling.models import (
    SkyModel,
    LogParabolaSpectralModel,
)
from gammapy.datasets import FluxPointsDataset, Datasets


# ============================================================
# INPUT FILES
# ============================================================

DATA_FILES = {
    "LHAASO J1825-1326": {
        "filename": "J1825_KM2A_201209.dat",
        "alpha": 0.92,
        "beta": 1.19,
    },
    "LHAASO J1908+0621": {
        "filename": "J1908_KM2A_201209.dat",
        "alpha": 2.27,
        "beta": 0.46,
    },
    "LHAASO J2226+6057": {
        "filename": "J2228_KM2A_201209.dat",
        "alpha": 1.56,
        "beta": 0.88,
    },
}


# ============================================================
# CONSTANTS
# ============================================================

REFERENCE = 10 * u.TeV

SED_TYPE = "e2dnde"


# ============================================================
# READ LHAASO TABLE
# ============================================================


def read_lhaaso_dat(filename):

    with open(filename, "r") as f:

        tokens = f.read().split()

    values = np.array(tokens, dtype=float)

    values = values.reshape(-1, 6)

    table = Table()

    table["e_ref"] = u.Quantity(
        values[:, 0] / 1e12,
        "TeV",
    )

    table["e2dnde"] = u.Quantity(
        values[:, 1],
        "erg cm-2 s-1",
    )

    table["e2dnde_errp"] = u.Quantity(
        values[:, 2],
        "erg cm-2 s-1",
    )

    table["e2dnde_errn"] = u.Quantity(
        values[:, 3],
        "erg cm-2 s-1",
    )

    table["e_min"] = u.Quantity(
        values[:, 4] / 1e12,
        "TeV",
    )

    table["e_max"] = u.Quantity(
        values[:, 5] / 1e12,
        "TeV",
    )

    table.meta["SED_TYPE"] = "e2dnde"

    return table


# ============================================================
# FIT FUNCTION
# ============================================================


def fit_logparabola_amplitude(source_name, config):

    filename = config["filename"]

    alpha = config["alpha"]
    beta = config["beta"]

    print("=" * 60)
    print(source_name)
    print("=" * 60)

    table = read_lhaaso_dat(filename)

    flux_points = FluxPoints.from_table(
        table,
        sed_type=SED_TYPE,
    )

    # ========================================================
    # MODEL
    # ========================================================

    spectral_model = LogParabolaSpectralModel(
        amplitude=1e-12 * u.Unit("cm-2 s-1 TeV-1"),
        reference=REFERENCE,
        alpha=alpha,
        beta=beta,
    )

    # Freeze shape parameters from paper
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

    # ========================================================
    # FIT
    # ========================================================

    fit = Fit()

    result = fit.run([dataset])

    print(result)

    print()
    print("Best-fit parameters")
    print(dataset.models.parameters.to_table())

    print()

    amplitude = spectral_model.amplitude.quantity

    print(f"Amplitude = {amplitude:.3e}")

    return dataset


# ============================================================
# RUN ALL SOURCES
# ============================================================


datasets = Datasets()

for source_name, config in DATA_FILES.items():

    dataset = fit_logparabola_amplitude(
        source_name,
        config,
    )

    datasets.append(dataset)


datasets.write(filename="datasets.yaml", filename_models="models.yaml")