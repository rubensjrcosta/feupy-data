# feupy-data

[![feupy](https://img.shields.io/badge/powered%20by-feupy-blue.svg?style=flat)](https://github.com/rubensjrcosta/feupy)
[![gammapy](https://img.shields.io/badge/powered%20by-gammapy-orange.svg?style=flat)](https://gammapy.org/)

This repository contains **datasets used by the feupy project**.

The main **feupy** repository is available at:

https://github.com/rubensjrcosta/feupy

Large datasets are stored separately from the main code repository to keep the package lightweight and to ensure reproducibility of simulations, examples, and analysis workflows.

---

## Dependency on Gammapy datasets

The **feupy** package is built on top of Gammapy.  
Therefore, **Gammapy datasets are required** to run many examples and simulations.

Users must configure both environment variables:

```
GAMMAPY_DATA
FEUPY_DATA
```

Example configuration:

```
GAMMAPY_DATA=/home/phoenix/Coding/data/gammapy-datasets/2.0
FEUPY_DATA=/home/phoenix/Coding/data/feupy-datasets/1.0
```

---

## Repository structure

Datasets are organized by version.

Example:

```
data/
   feupy-datasets/
      1.0/
         catalogs/
         irfs/
```

Typical dataset contents may include:

- CTAO simulation products
- GRB spectral models
- instrument response functions (IRFs)
- example event lists
- auxiliary analysis data

---

## Installation

Clone the repository:

```
git clone https://github.com/rubensjrcosta/feupy-data.git
```

Place the datasets in a local directory such as:

```
~/Coding/data/feupy-datasets/
```

Example directory structure:

```
~/Coding/data/
   gammapy-datasets/
      2.0/
   feupy-datasets/
      1.0/
```

---

## Usage in Python

Datasets can be accessed through the environment variables:

```python
import os
from pathlib import Path

GAMMAPY_DATA = Path(os.environ["GAMMAPY_DATA"])
FEUPY_DATA = Path(os.environ["FEUPY_DATA"])
```

---

## License

This repository follows the same license as the main **feupy** project.
