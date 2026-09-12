# FeuPy Data

[![FeuPy](https://img.shields.io/badge/used%20by-FeuPy-blue.svg)](https://github.com/rubensjrcosta/feupy)

**FeuPy Data** contains auxiliary datasets used by [FeuPy](https://github.com/rubensjrcosta/feupy), an open-source Python package for very-high-energy gamma-ray analysis, modeling, and simulations.

The repository provides external data required by selected FeuPy workflows, including catalog information, instrument response functions, sensitivity products, and other supporting datasets.

## Repository structure

The datasets are organized by version:

```text
feupy-data/
└── feupy-datasets/
    └── 1.0/
```

Each dataset release is stored in a dedicated version directory to ensure reproducibility and compatibility with specific FeuPy releases.

## Dataset versions

The current dataset release is:

```text
feupy-datasets/1.0/
```

Compatibility with FeuPy releases is summarized below:

| FeuPy version | FeuPy Data version |
| ------------- | ------------------ |
| `v0.1.0`      | `1.0`              |

## Installation

Clone the repository:

```bash
git clone https://github.com/rubensjrcosta/feupy-data.git
```

The data do not require installation as a Python package.

Instead, FeuPy accesses the datasets through the `FEUPY_DATA` environment variable.

## Configure `FEUPY_DATA`

Set the environment variable to the dataset version required by your FeuPy installation:

```bash
export FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

For example:

```bash
export FEUPY_DATA=$HOME/feupy-data/feupy-datasets/1.0
```

Verify the configuration with:

```bash
echo $FEUPY_DATA
```

## Conda environment configuration

When using a Conda environment, the data path can be stored directly in the environment:

```bash
conda env config vars set \
    FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

Reactivate the environment after setting the variable:

```bash
conda deactivate
conda activate feupy
```

Verify that the variable is available:

```bash
echo $FEUPY_DATA
```

## Usage with FeuPy

FeuPy automatically uses the `FEUPY_DATA` environment variable when access to external datasets is required.

For FeuPy `v0.1.0`, the expected configuration is:

```text
FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

The FeuPy source code and documentation are available at:

https://github.com/rubensjrcosta/feupy

## Reproducibility

Dataset versions are kept separate so that scientific analyses can be reproduced using the same data products.

Users are encouraged to report both the FeuPy software version and the FeuPy Data version used in their analyses.

For example:

```text
FeuPy v0.1.0
FeuPy Data 1.0
```

## Data provenance

The repository may contain data derived from or associated with external observatories, catalogs, scientific collaborations, publications, or software projects.

Where applicable, the corresponding original references should be cited when these datasets are used in scientific work.

Users should consult the documentation, metadata, and original sources associated with individual datasets for information about provenance and scientific interpretation.

## Citation

If you use FeuPy Data in scientific work, please cite FeuPy and the original references associated with the datasets used in your analysis.

Citation information for FeuPy is provided in the main repository:

https://github.com/rubensjrcosta/feupy

A dedicated citation record for FeuPy Data may also be provided through Zenodo.

## Versioning

FeuPy Data uses independent dataset versioning.

The software and dataset versions therefore do not need to match numerically.

For example:

```text
FeuPy software:     v0.1.0
FeuPy Data:         1.0
```

A new dataset version should be created whenever changes to the data may affect scientific results or compatibility with FeuPy analyses.

## License and data rights

The contents of this repository may originate from multiple external data providers.

Individual datasets may therefore be subject to different licenses, acknowledgments, citation requirements, or redistribution policies.

The presence of a dataset in this repository does not override the terms defined by the original data provider.

Users are responsible for consulting and following the applicable conditions associated with each dataset.

## Authors

* **Rubens Costa Jr.**
* **Rita C. dos Anjos**

## Related project

FeuPy source code:

https://github.com/rubensjrcosta/feupy
