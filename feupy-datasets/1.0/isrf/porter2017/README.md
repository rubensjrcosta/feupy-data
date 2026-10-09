# Galactic Interstellar Radiation Field — Porter et al. (2017)

This directory contains documentation for the Galactic interstellar
radiation field (ISRF) models described by Porter et al. (2017).

The models are used by FeuPy to evaluate Galactic photon fields
relevant to nonthermal emission processes, particularly inverse-Compton
scattering.

## Reference

Porter, T. A., Jóhannesson, G., & Moskalenko, I. V. (2017).

*High-Energy Gamma Rays from the Milky Way: Three-Dimensional Spatial
Models for the Cosmic-Ray and Radiation Field Densities in the
Interstellar Medium.*

The Astrophysical Journal, 846, 67.

DOI: https://doi.org/10.3847/1538-4357/aa844d

## Data source

The original ISRF data are distributed by the GALPROP collaboration.

Official website:

https://galprop.stanford.edu/

The dataset includes the F98 and R12 Galactic ISRF configurations.

## Data availability

The original GALPROP scientific files are not redistributed through
FeuPy Data.

Users must obtain the data from the official GALPROP distribution
and comply with its applicable terms of use.

## Directory structure

After obtaining and extracting the original dataset, the expected
directory structure is:

```text
porter2017/
├── README.md
└── Porter_etal_ApJ_846_67_2017_SEDonly/
    ├── F98/
    ├── R12/
    ├── README
    └── extract_number_density.cc
```

The `Porter_etal_ApJ_846_67_2017_SEDonly/` directory is excluded
from Git version control.

## Configuration

FeuPy locates the data through the `FEUPY_DATA` environment variable.

For FeuPy Data 1.0:

```bash
export FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

The original dataset must be placed under:

```text
$FEUPY_DATA/isrf/porter2017/
```

## Usage with FeuPy

FeuPy provides the `Porter2017ISRF` interface for accessing
the Galactic radiation fields.

The implementation uses `astropy.coordinates.SkyCoord` to specify
Galactic positions.

Consult the FeuPy documentation for the supported methods and
model configurations.

## Testing

From the FeuPy source directory:

```bash
python -m pytest feupy/isrf/tests/ -v -rs
```

Tests requiring the original GALPROP data can only run when
the corresponding files are available.

## Citation

When using these radiation fields in scientific work, cite
Porter et al. (2017) and follow the citation requirements
specified by the GALPROP collaboration.

FeuPy Data should also be cited when its data organization
or supporting materials are used.

FeuPy Data DOI:

https://doi.org/10.5281/zenodo.22723056