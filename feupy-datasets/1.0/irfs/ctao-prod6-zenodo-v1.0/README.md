# CTAO Prod6 v1.0 Instrument Response Functions

This directory contains documentation for the Cherenkov Telescope
Array Observatory (CTAO) Prod6 v1.0 instrument response functions
(IRFs) used by FeuPy.

## Overview

CTAO Prod6 provides instrument response functions for simulations
and performance studies of the CTAO North and South arrays.

The available configurations include different observation
conditions and instrument settings.

FeuPy provides an interface for selecting and managing these
response functions through `CTAOIRFManager`.

## Data source

The original instrument response functions are distributed
through the corresponding CTAO Prod6 data release.

Official CTAO website:

https://www.ctao.org/

Users should consult the original release documentation for
information about the instrument configurations, simulation
assumptions, data access, and citation requirements.

## Data availability

The original Prod6 IRF files are not redistributed through
this repository at present.

Users must obtain the corresponding files from their
official distribution and comply with the applicable
data-use and redistribution conditions.

## Directory structure

The expected location is:

```text
feupy-datasets/
└── 1.0/
    └── irfs/
        └── ctao-prod6-zenodo-v1.0/
            ├── README.md
            └── [original Prod6 IRF files]
```

The original IRF files are excluded from Git version control.

## Configuration

Set the `FEUPY_DATA` environment variable:

```bash
export FEUPY_DATA=/path/to/feupy-data/feupy-datasets/1.0
```

FeuPy will use this directory to locate the corresponding
instrument response files.

## Usage with FeuPy

```python
from feupy.irf import CTAOIRFManager


prod6_dark = CTAOIRFManager(
    production="prod6",
    condition="dark",
)

prod6_halfmoon = CTAOIRFManager(
    production="prod6",
    condition="halfmoon",
)
```

The available configurations depend on the installed IRF files.

## Testing

From the FeuPy source directory:

```bash
python -m pytest feupy/irf/tests/ -v -rs
```

Tests requiring external IRF files may be skipped when
the corresponding datasets are unavailable.

## Citation

When using these instrument response functions in scientific
work, cite the corresponding CTAO Prod6 data release and
follow its citation requirements.

FeuPy Data should also be cited when its data organization
or supporting materials are used.

FeuPy Data DOI:

https://doi.org/10.5281/zenodo.22723056