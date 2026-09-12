# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Generate the pulsar_spectra catalog used by FeuPy."""

from pathlib import Path

import numpy as np
import yaml
from pulsar_spectra.catalogue import collect_catalogue_fluxes

BASE_DIR = Path(__file__).resolve().parent
CATALOG_FILE = BASE_DIR / "pulsar_spectra.yaml"


def convert_numpy_objects(obj):
    """Recursively convert NumPy objects to YAML-safe Python types.

    Parameters
    ----------
    obj : object
        Object to convert.

    Returns
    -------
    object
        Object containing only plain Python types.
    """
    if isinstance(obj, np.ndarray):
        return obj.tolist()

    if isinstance(obj, np.generic):
        return obj.item()

    if isinstance(obj, dict):
        return {key: convert_numpy_objects(value) for key, value in obj.items()}

    if isinstance(obj, (list, tuple)):
        return [convert_numpy_objects(value) for value in obj]

    return obj


def make_catalog():
    """Collect and prepare the pulsar spectral catalog."""
    catalog = collect_catalogue_fluxes()
    return convert_numpy_objects(catalog)


def write_catalog(filename=CATALOG_FILE):
    """Write the pulsar spectral catalog to YAML.

    Parameters
    ----------
    filename : str or `~pathlib.Path`, optional
        Output YAML filename.
    """
    filename = Path(filename)
    catalog = make_catalog()

    with filename.open("w", encoding="utf-8") as yaml_file:
        yaml.safe_dump(
            catalog,
            yaml_file,
            default_flow_style=False,
            sort_keys=True,
        )

    print(f"Pulsar spectral data saved to {filename}")


if __name__ == "__main__":
    write_catalog()
