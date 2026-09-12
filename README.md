# FeuPy Data

[![DOI](https://zenodo.org/badge/1177404918.svg)](https://doi.org/10.5281/zenodo.22723056)

FeuPy Data is the auxiliary data repository for
[FeuPy](https://github.com/rubensjrcosta/feupy), providing versioned
datasets used by the package for gamma-ray source catalogs, instrument
response functions, and data products from dedicated scientific
publications.

The data repository is maintained separately from the FeuPy source code
so that software and dataset versions can evolve independently while
preserving the reproducibility of scientific analyses.

## Repository structure

The repository is organized into versioned dataset releases:

```text
feupy-data/
├── CITATION.cff
├── LICENSE
├── README.md
└── feupy-datasets/
    └── 1.0/
        ├── catalogs/
        ├── dedicated_publications/
        └── irfs/
```

The main directories contain:

- `catalogs/`: gamma-ray and multiwavelength source catalogs and
  associated data products;
- `dedicated_publications/`: data products associated with specific
  scientific publications;
- `irfs/`: instrument response functions and related files used by
  FeuPy.

Individual directories may also contain scripts, metadata, README files,
figures, and original or derived data products required to document the
provenance and construction of the datasets.

## Dataset version

The current dataset release is:

```text
FeuPy Data 1.0
```

FeuPy Data `1.0` is the dataset release associated with the initial
FeuPy `v0.1.0` release.

The recommended combination is therefore:

```text
FeuPy:       v0.1.0
FeuPy Data:  1.0
```

## Installation

Clone the FeuPy Data repository:

```bash
git clone https://github.com/rubensjrcosta/feupy-data.git
```

The datasets for version `1.0` are located in:

```text
feupy-data/feupy-datasets/1.0
```

FeuPy Data is not installed as a Python package. FeuPy accesses the
datasets through the `FEUPY_DATA` environment variable.

## Configuring `FEUPY_DATA`

Set `FEUPY_DATA` to the directory corresponding to the dataset version
that you want to use.

For example:

```bash
export FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

If you are using a Conda environment, the variable can be stored in the
environment:

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

FeuPy automatically uses the `FEUPY_DATA` environment variable when
access to external datasets is required.

For FeuPy `v0.1.0`, the expected configuration is:

```text
FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

The FeuPy source code and documentation are available at:

https://github.com/rubensjrcosta/feupy

## Reproducibility

FeuPy Data releases are versioned independently from the FeuPy software.

This separation allows a scientific analysis to be reproduced using the
same software and data products even after either repository has
subsequently changed.

Users are encouraged to report both versions when presenting or
publishing results obtained with FeuPy.

For example:

```text
FeuPy v0.1.0
FeuPy Data 1.0
```

When possible, analyses should also record the specific versions of
external catalogs, instrument response functions, and publication data
products used.

## Data provenance

FeuPy Data contains data products derived from or associated with
external observatories, source catalogs, scientific collaborations,
publications, and software projects.

The repository preserves, where applicable, supporting information such
as:

- bibliographic references;
- source and publication metadata;
- original or processed data products;
- scripts used to construct FeuPy-compatible datasets;
- information about dataset availability and review status;
- figures and documentation associated with the original data products.

These materials are retained to improve traceability and
reproducibility.

The inclusion of a dataset in FeuPy Data does not replace the original
scientific publication or data release. Users should consult and cite
the corresponding original sources when using these data products in
scientific work.

## Citation

If you use FeuPy Data in scientific work, please cite both **FeuPy Data**
and the original references associated with the datasets used in your
analysis.

Citation metadata for this repository are provided in:

```text
CITATION.cff
```

The archived release and DOI will be provided through Zenodo.

FeuPy software is available at:

https://github.com/rubensjrcosta/feupy

When reporting an analysis, we recommend specifying both the software
and dataset versions, for example:

```text
FeuPy v0.1.0
FeuPy Data 1.0
```

In addition, the appropriate publications, observatories, catalogs, and
collaborations associated with the individual datasets should be cited
according to their respective citation requirements.

## Versioning

FeuPy Data uses independent dataset versioning.

Software and dataset versions therefore do not need to match
numerically.

For the initial release:

```text
FeuPy software:  v0.1.0
FeuPy Data:      1.0
```

A new FeuPy Data version should be created whenever changes to the
datasets may affect scientific results, reproducibility, or
compatibility with FeuPy analyses.

Minor maintenance changes that do not modify the scientific content of
a released dataset should be documented appropriately without altering
previous archived releases.

Released versions should remain immutable so that analyses referring to
a specific FeuPy Data release can be reproduced.

## License and data rights

The FeuPy Data repository structure, scripts, and original project
materials are distributed under the BSD 3-Clause License, unless
otherwise stated.

The repository also contains or references data products originating
from external observatories, catalogs, scientific collaborations,
publications, and software projects. Such third-party data may be
subject to their own licenses, terms of use, acknowledgment
requirements, citation requirements, or redistribution policies.

The BSD 3-Clause License of this repository does not supersede the
rights or conditions associated with third-party data products.

Users are responsible for consulting the provenance information and
original references associated with each dataset before redistribution
or scientific publication.

See the `LICENSE` file for the license applicable to the original FeuPy
Data repository content.

## Contributing

Contributions that improve dataset quality, provenance information,
reproducibility, or compatibility with FeuPy are welcome.

When adding or modifying a dataset, contributors should preserve the
original scientific provenance and, whenever possible, provide:

- the original reference or data source;
- sufficient metadata to identify the dataset;
- scripts required to reproduce derived products;
- documentation describing relevant transformations;
- appropriate citation information.

Changes that modify scientific data products should be clearly
documented and considered when assigning a new FeuPy Data version.

## Related project

FeuPy Data is maintained as the companion data repository for FeuPy:

https://github.com/rubensjrcosta/feupy
