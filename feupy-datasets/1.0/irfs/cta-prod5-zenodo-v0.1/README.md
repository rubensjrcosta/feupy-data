cat > feupy-datasets/1.0/irfs/cta-prod5-zenodo-v0.1/README.md <<'EOF'
# CTAO Instrument Response Functions — Prod5 v0.1

## Overview

This directory contains the CTAO Prod5 v0.1 Instrument Response
Functions (IRFs) in FITS format.

The IRFs are used by FeuPy for gamma-ray astronomy simulations
and sensitivity studies.

## Original dataset

**Title:** CTAO Instrument Response Functions - prod5 version v0.1

**Creators:** Cherenkov Telescope Array Observatory and
Cherenkov Telescope Array Consortium

**Version:** v0.1

**DOI:** https://doi.org/10.5281/zenodo.5499840

**License:** Creative Commons Attribution 4.0 International

**License URL:** https://creativecommons.org/licenses/by/4.0/

## Instrument configurations

The dataset provides IRFs for:

- CTA North and CTA South.
- Zenith angles of 20, 40, and 60 degrees.
- AverageAz, NorthAz, and SouthAz configurations.
- Observation durations of 0.5, 5, and 50 hours.
- Different telescope subarrays.

## Data provenance

The original FITS-only distribution is available from:

https://zenodo.org/records/5499840

The original data are provided by the CTA Observatory and
CTA Consortium.

Users should cite the original Zenodo dataset and follow
its citation and acknowledgement instructions.

## License and redistribution

The original dataset is distributed under the Creative
Commons Attribution 4.0 International license.

Redistribution requires appropriate attribution to the
original creators, preservation of applicable notices,
and indication of any modifications.

FeuPy Data is an independent scientific data collection
and does not imply endorsement by the CTA Observatory.

## Usage

Set the FEUPY_DATA environment variable to the FeuPy
dataset root directory.

The CTAOIRFManager class in FeuPy provides access to
the supported instrument response configurations.
EOF