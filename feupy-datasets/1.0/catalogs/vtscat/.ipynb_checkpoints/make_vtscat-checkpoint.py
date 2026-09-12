"""Convert VTSCat YAML source files to an ECSV catalog.

VTSCat is the VERITAS Catalog of gamma-ray observations described in:

https://iopscience.iop.org/article/10.3847/2515-5172/acb147
"""

import logging
from pathlib import Path

import astropy.units as u
from astropy.table import Column, Table

from feupy.utils.io import read_yaml

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


BASE_DIR = Path(__file__).resolve().parent
DATASETS_PATH = BASE_DIR / "datasets"
SOURCES_PATH = BASE_DIR / "sources"

VTSCAT_DICT = {
    "detect": "tev-0",
    "non_detect": "tev-1",
    "crs": "tev-3",
    "all": "tev-",
}


def read_vtscat_sources(which="all", sources_path=SOURCES_PATH):
    """
    Read VERITAS sources from VTSCat YAML files.

    Parameters
    ----------
    which : str, optional
        Source category to read. Valid options are ``detect``,
        ``non_detect``, ``crs``, and ``all``.
    sources_path : pathlib.Path, optional
        Directory containing the VTSCat YAML source files.

    Returns
    -------
    data_list : list of dict
        Parsed source data.

    Raises
    ------
    ValueError
        If ``which`` is not a valid VTSCat category.
    FileNotFoundError
        If no matching YAML files are found.
    """
    if which not in VTSCAT_DICT:
        valid_options = list(VTSCAT_DICT)
        raise ValueError(
            f"Invalid category '{which}'. Valid options are {valid_options}."
        )

    sources_path = Path(sources_path)
    prefix = VTSCAT_DICT[which]

    filenames = sorted(
        filename
        for filename in sources_path.iterdir()
        if filename.name.startswith(prefix) and filename.suffix == ".yaml"
    )

    if not filenames:
        raise FileNotFoundError(
            f"No matching files found for key '{which}' "
            f"in directory '{sources_path}'."
        )

    data_list = []

    for filename in filenames:
        data = read_yaml(filename)
        data_list.append(data)

        source_name = data.get("source_name", filename.name)
        log.info("Loaded source: %s from %s", source_name, filename.name)

    return data_list


def flatten_data(data):
    """
    Flatten the nested VTSCat source structure.

    Parameters
    ----------
    data : dict
        VTSCat source data.

    Returns
    -------
    flattened : dict
        Flattened source information.
    """
    return {
        "veritas_id": data.get("source_id"),
        "common_name": data.get("common_name", "Unknown"),
        "veritas_name": data.get("veritas_name", {}).get("name", "Unknown"),
        "veritas_components": data.get("veritas_name", {}).get(
            "components",
            "Unknown",
        ),
        "other_names": ", ".join(data.get("other_names", ["Unknown"])),
        "where": data.get("where", "Unknown"),
        "simbad_id": data.get("pos", {}).get("simbad_id", "Unknown"),
        "ra": data.get("pos", {}).get("ra"),
        "dec": data.get("pos", {}).get("dec"),
        "reference_id": ", ".join(
            data.get("reference_id", ["Unknown"]),
        ),
    }


def make_catalog():
    """
    Create the VTSCat catalog table.

    Returns
    -------
    table : astropy.table.Table
        VTSCat catalog table.
    """
    data_list = read_vtscat_sources()
    flattened_data = [flatten_data(data) for data in data_list]

    columns = {
        "veritas_id": Column(
            [data["veritas_id"] for data in flattened_data],
            dtype="int",
        ),
        "common_name": Column(
            [data["common_name"] for data in flattened_data],
            dtype="str",
            length=20,
        ),
        "veritas_name": Column(
            [data["veritas_name"] for data in flattened_data],
            dtype="str",
            length=20,
        ),
        "veritas_components": Column(
            [data["veritas_components"] for data in flattened_data],
            dtype="str",
            length=20,
        ),
        "other_names": Column(
            [data["other_names"] for data in flattened_data],
            dtype="str",
            length=50,
        ),
        "where": Column(
            [data["where"] for data in flattened_data],
            dtype="str",
            length=10,
        ),
        "simbad_id": Column(
            [data["simbad_id"] for data in flattened_data],
            dtype="str",
            length=20,
        ),
        "ra": Column(
            [data["ra"] for data in flattened_data],
            unit=u.deg,
            dtype="float",
        ),
        "dec": Column(
            [data["dec"] for data in flattened_data],
            unit=u.deg,
            dtype="float",
        ),
        "reference_id": Column(
            [data["reference_id"] for data in flattened_data],
            dtype="str",
            length=50,
        ),
    }

    table = Table(columns)

    table.meta["catalog_name"] = "vtscat"
    table.meta["comments"] = [
        "Reference: https://zenodo.org/records/6163391",
    ]

    table.sort("veritas_id")

    table["ra"].description = "Right Ascension (J2000)"
    table["ra"].format = ".3f"

    table["dec"].description = "Declination (J2000)"
    table["dec"].format = ".3f"

    table["veritas_id"].description = (
        "Unique identifier of an object (integer)"
    )
    table["common_name"].description = (
        "Common name as frequently used in literature"
    )
    table["veritas_name"].description = (
        "VERITAS name as registered in the AU Registry"
    )
    table["veritas_components"].description = (
        "VERITAS source components"
    )
    table["other_names"].description = (
        "Other names used in literature or catalogs"
    )
    table["where"].description = (
        "Galactic (gal) or extragalactic (egal) object"
    )
    table["simbad_id"].description = "SIMBAD identifier"
    table["reference_id"].description = (
        "List of references for this catalog"
    )

    table["source_name"] = [
        (
            row["veritas_name"]
            if row["veritas_name"] != "Unknown"
            else row["common_name"]
        )
        for row in table
    ]
    table["source_name"].description = (
        'Source name: "veritas_name" if available, '
        'else "common_name"'
    )

    table["type"] = [
        (
            "detected"
            if row["veritas_id"] < 100000
            else "non_detected"
            if row["veritas_id"] < 300000
            else "crs"
        )
        for row in table
    ]
    table["type"].description = "VERITAS source type"

    return table[
        "source_name",
        "ra",
        "dec",
        "type",
        "where",
        "veritas_name",
        "veritas_components",
        "veritas_id",
        "common_name",
        "other_names",
        "simbad_id",
        "reference_id",
    ]


def write_catalog():
    """Write the VTSCat catalog in ECSV format."""
    SOURCES_PATH.mkdir(parents=True, exist_ok=True)
    DATASETS_PATH.mkdir(parents=True, exist_ok=True)

    table = make_catalog()

    output_path = SOURCES_PATH / "vtscat_catalog.ecsv"

    table.write(
        output_path,
        format="ascii.ecsv",
        overwrite=True,
    )

    log.info("Table saved as ECSV: %s", output_path)


if __name__ == "__main__":
    write_catalog()