# FeuPy Data

[![DOI](https://zenodo.org/badge/1177404918.svg)](https://doi.org/10.5281/zenodo.22723056)

**FeuPy Data** is the companion data repository for
[FeuPy](https://github.com/rubensjrcosta/feupy), a Python package
for high-energy and very-high-energy gamma-ray astrophysics.

The repository provides versioned scientific datasets used by FeuPy,
including gamma-ray source catalogs, instrument response functions
(IRFs), interstellar radiation fields (ISRFs), and data products
associated with dedicated scientific publications.

FeuPy Data is maintained separately from the FeuPy source code so
that software and dataset versions can evolve independently while
preserving the reproducibility of scientific analyses.

The repository also provides a standardized directory structure
for organizing external scientific datasets and their associated
metadata, documentation, and supporting files.

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
        ├── irfs/
        │   └── ctao-prod6-zenodo-v1.0/
        └── isrf/
            └── porter2017/
```

The main directories contain:

- `catalogs/`: gamma-ray and multiwavelength source catalogs and
  associated data products;
- `dedicated_publications/`: data products associated with specific
  scientific publications;
- `irfs/`: instrument response functions and related files used
  in FeuPy simulations and analyses;
- `isrf/`: interstellar radiation field models used in radiative
  emission calculations.

Individual directories may also contain scripts, metadata, README
files, figures, and original or derived data products required to
document the provenance and construction of the datasets.

The exact contents of each directory depend on the corresponding
scientific data release.

## Dataset version

The current dataset release is:

```text
FeuPy Data 1.0
```

FeuPy Data `1.0` is the dataset release associated with the initial
FeuPy `v0.1.0` release.

The recommended combination for the initial release is:

```text
FeuPy:       v0.1.0
FeuPy Data:  1.0
```

Subsequent FeuPy development versions may support additional
datasets while retaining compatibility with the same dataset
release.

Users should verify compatibility with the FeuPy version used
in their analyses.

## Installation

Clone the FeuPy Data repository:

```bash
git clone https://github.com/rubensjrcosta/feupy-data.git
```

The datasets for version `1.0` are located in:

```text
feupy-data/feupy-datasets/1.0
```

FeuPy Data is not installed as a Python package.

Instead, FeuPy accesses the datasets through the `FEUPY_DATA`
environment variable.

Some scientific datasets may require additional downloads,
extraction, or preparation depending on their distribution
and availability.

Users should verify that the required files are present before
running analyses that depend on external datasets.

## Configuring `FEUPY_DATA`

Set `FEUPY_DATA` to the directory corresponding to the dataset
version that you want to use.

For example:

```bash
export FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

If you are using a Conda environment, the variable can be stored
in the environment:

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

The expected output is:

```text
/path/to/feupy-data/feupy-datasets/1.0
```

The variable must point to the versioned dataset directory,
not to the root of the Git repository.

## Scientific datasets

FeuPy Data organizes several categories of scientific datasets
used by FeuPy.

### Gamma-ray source catalogs

The `catalogs/` directory contains gamma-ray and multiwavelength
source catalogs and associated data products.

These datasets may include source positions, spectral properties,
morphological information, flux measurements, and other quantities
relevant to gamma-ray astrophysics.

Catalogs are organized according to their original sources
and data releases.

Users should consult the corresponding documentation and
original references before using catalog data in scientific
publications.

### Dedicated scientific publications

The `dedicated_publications/` directory contains data products
associated with individual scientific publications.

These may include observational measurements, spectral energy
distributions, morphological information, model parameters,
and supporting files required to reproduce published analyses.

The repository aims to preserve the original scientific
provenance of these data products.

### Instrument response functions

The `irfs/` directory contains instrument response functions
used in gamma-ray instrument simulations and analyses.

FeuPy provides support for CTAO instrument response functions,
including the Prod5 and Prod6 simulation productions.

#### CTAO Prod5

CTAO Prod5 instrument response functions provide reference
configurations for CTAO performance studies.

Depending on the available files, the configurations may include:

- CTAO North and South arrays;
- different zenith angles;
- different observation times;
- azimuth-dependent or azimuth-averaged responses.

FeuPy provides utilities for selecting and managing these
instrument response configurations.

The corresponding files must be available in the directory
structure expected by the installed FeuPy version.

#### CTAO Prod6 v1.0

FeuPy also supports the CTAO Prod6 v1.0 instrument response
functions.

The corresponding dataset is organized under:

```text
feupy-datasets/1.0/irfs/ctao-prod6-zenodo-v1.0/
```

Prod6 provides updated CTAO instrument response configurations,
including different observing conditions.

The FeuPy implementation supports configurations associated
with dark-sky and half-moon observations.

For example:

```python
from feupy.irf import CTAOIRFManager

prod5 = CTAOIRFManager(
    production="prod5",
)

prod6_dark = CTAOIRFManager(
    production="prod6",
    condition="dark",
)

prod6_halfmoon = CTAOIRFManager(
    production="prod6",
    condition="halfmoon",
)
```

The required IRF files must be available in their expected
locations.

Users should consult the original CTAO data release for
information about the instrument configurations, simulation
assumptions, data availability, and citation requirements.

Additional information about CTAO is available at:

https://www.ctao.org/

### Interstellar radiation fields

The `isrf/` directory contains interstellar radiation field
models used in nonthermal radiative emission calculations.

These photon fields are relevant to processes such as
inverse-Compton scattering by relativistic electrons.

#### Porter et al. (2017)

FeuPy provides an interface to the Galactic interstellar
radiation field models described by Porter et al. (2017).

The corresponding data are organized under:

```text
feupy-datasets/1.0/isrf/porter2017/
```

The original GALPROP dataset contains the F98 and R12
model configurations.

A typical directory structure is:

```text
porter2017/
└── Porter_etal_ApJ_846_67_2017_SEDonly/
    ├── F98/
    ├── R12/
    ├── README
    └── extract_number_density.cc
```

The FeuPy implementation provides the `Porter2017ISRF`
interface for evaluating radiation fields at Galactic
positions specified using `astropy.coordinates.SkyCoord`.

Supported functionality includes:

- evaluation of radiation energy densities;
- access to spectral energy distributions;
- evaluation of individual radiation-field components;
- blackbody approximations of the radiation field;
- construction of thermal photon fields for Naima.

The blackbody approximation can be useful when modeling
inverse-Compton emission from relativistic electron populations.

For example:

```python
import astropy.units as u

from astropy.coordinates import SkyCoord

from feupy.isrf import Porter2017ISRF


position = SkyCoord(
    l=17.8 * u.deg,
    b=-0.7 * u.deg,
    distance=4.0 * u.kpc,
    frame="galactic",
)

isrf = Porter2017ISRF(
    model="R12",
)

energy_density = isrf.energy_density(
    position,
)

print(energy_density)
```

The corresponding GALPROP files must be available in the
directory structure expected by FeuPy.

The original publication and associated data documentation
should be consulted for information about the physical
assumptions, model configurations, and citation requirements.

## Usage with FeuPy

FeuPy automatically uses the `FEUPY_DATA` environment variable
when access to external datasets is required.

For FeuPy `v0.1.0`, the expected configuration is:

```text
FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

The environment variable provides a common entry point for
locating scientific datasets independently of the FeuPy
installation directory.

This allows users to maintain separate software environments
while sharing the same versioned scientific datasets.

The FeuPy source code and documentation are available at:

https://github.com/rubensjrcosta/feupy

## Testing and data validation

FeuPy includes unit tests and regression tests for scientific
functionality.

Some tests operate independently of external scientific data,
while others require the corresponding datasets to be available.

For example, regression tests for the Porter et al. (2017)
ISRF implementation use reference quantities calculated
from the original GALPROP data.

The required files must be available for these tests to run.

To execute the ISRF tests from the FeuPy source directory:

```bash
python -m pytest feupy/isrf/tests/ -v
```

To execute the IRF tests:

```bash
python -m pytest feupy/irf/tests/ -v
```

To execute the complete FeuPy test suite:

```bash
python -m pytest -q
```

Tests requiring external data may be skipped when the
corresponding datasets are unavailable, depending on the
test configuration.

A successful test run should therefore be interpreted
together with the number of executed and skipped tests.

Users are encouraged to validate the availability and
integrity of the scientific datasets before performing
production analyses.

## Reproducibility

FeuPy Data releases are versioned independently from the
FeuPy software.

This separation allows scientific analyses to be reproduced
using the same software and data products even after either
repository has subsequently changed.

Users are encouraged to report both versions when presenting
or publishing results obtained with FeuPy.

For example:

```text
FeuPy v0.1.0
FeuPy Data 1.0
```

When possible, analyses should also record:

- the FeuPy software version or Git commit;
- the FeuPy Data release or Git commit;
- the original dataset version;
- the instrument response configuration;
- the physical model assumptions;
- the relevant bibliographic references.

For CTAO analyses, relevant metadata may include the IRF
production, array configuration, zenith angle, observation
time, and observing conditions.

For ISRF analyses, relevant metadata may include the GALPROP
model, Galactic position, radiation-field components, and
parameters used in blackbody approximations.

Recording these details improves the reproducibility and
interpretability of scientific results.

## Data provenance

FeuPy Data contains data products derived from or associated
with external observatories, source catalogs, scientific
collaborations, publications, and software projects.

The repository preserves, where applicable, supporting
information such as:

- bibliographic references;
- source and publication metadata;
- original or processed data products;
- scripts used to construct FeuPy-compatible datasets;
- information about dataset availability and review status;
- figures and documentation associated with the original
  data products.

These materials are retained to improve traceability and
reproducibility.

The inclusion of a dataset in FeuPy Data does not replace
the original scientific publication or data release.

Users should consult and cite the corresponding original
sources when using these data products in scientific work.

## Citation

If you use FeuPy Data in scientific work, please cite both
**FeuPy Data** and the original references associated with
the datasets used in your analysis.

FeuPy Data is archived through Zenodo:

**DOI:** https://doi.org/10.5281/zenodo.22723056

Citation metadata for this repository are provided in:

```text
CITATION.cff
```

The FeuPy software repository is available at:

https://github.com/rubensjrcosta/feupy

When reporting an analysis, we recommend specifying both
the software and dataset versions, for example:

```text
FeuPy v0.1.0
FeuPy Data 1.0
```

In addition, the appropriate publications, observatories,
catalogs, and collaborations associated with the individual
datasets should be cited according to their respective
citation requirements.

## Versioning

FeuPy Data uses independent dataset versioning.

Software and dataset versions therefore do not need to match
numerically.

For the initial release:

```text
FeuPy software:  v0.1.0
FeuPy Data:      1.0
```

A new FeuPy Data version should be created whenever changes
to the datasets may affect scientific results, reproducibility,
or compatibility with FeuPy analyses.

Minor maintenance changes that do not modify the scientific
content of a released dataset should be documented
appropriately without altering previous archived releases.

Released versions should remain immutable so that analyses
referring to a specific FeuPy Data release can be reproduced.

## License and data rights

The FeuPy Data repository structure, scripts, and original
project materials are distributed under the BSD 3-Clause
License, unless otherwise stated.

The repository also contains or references data products
originating from external observatories, catalogs, scientific
collaborations, publications, and software projects.

Such third-party data may be subject to their own licenses,
terms of use, acknowledgment requirements, citation
requirements, or redistribution policies.

The BSD 3-Clause License of this repository does not
supersede the rights or conditions associated with
third-party data products.

Users are responsible for consulting the provenance
information and original references associated with
each dataset before redistribution or scientific publication.

See the `LICENSE` file for the license applicable to the
original FeuPy Data repository content.

## Contributing

Contributions that improve dataset quality, provenance
information, reproducibility, or compatibility with FeuPy
are welcome.

When adding or modifying a dataset, contributors should
preserve the original scientific provenance and, whenever
possible, provide:

- the original reference or data source;
- sufficient metadata to identify the dataset;
- scripts required to reproduce derived products;
- documentation describing relevant transformations;
- appropriate citation information.

Changes that modify scientific data products should be
clearly documented and considered when assigning a new
FeuPy Data version.

## Related project

FeuPy Data is maintained as the companion data repository
for FeuPy:

https://github.com/rubensjrcosta/feupy