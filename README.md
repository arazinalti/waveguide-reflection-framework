# Waveguide Reflection Framework

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Overview

This repository contains the complete code implementation for the paper:

**"A Generalized Reflection-Count-Based Geometrical Optics Framework for Attenuation Analysis in Multimode Waveguides"**

📌 **Manuscript Status:** Submitted to *Journal of the Optical Society of America B (JOSA B)* – Under Quality Check (July 2026)

## 📊 Mathematical Model

The total number of internal reflections in a planar waveguide is:

$$N = \frac{L \tan \theta}{2h}$$

The transmitted power is modeled as:

$$P(L, \theta) = P_0 \exp\left[-L \left( \frac{\alpha_{abs}}{\cos\theta} + \frac{\alpha_{sc} \tan\theta}{2h} \right)\right]$$

## 🚀 Features

- ✅ Analytical calculation of internal reflection count
- ✅ Two-parameter attenuation model
- ✅ Optimal launch angle optimization
- ✅ Mode-dependent loss (MDL) analysis
- ✅ Bending loss extension
- ✅ Wavelength-dependent analysis
- ✅ Monte Carlo ray-tracing simulation
- ✅ Comprehensive figure generation

## 📦 Installation

```bash
git clone https://github.com/arazinalti/waveguide-reflection-framework.git
cd waveguide-reflection-framework
pip install -r requirements.txt
```

## 🎯 Quick Start

```python
from src.waveguide import Waveguide
import numpy as np

wg = Waveguide(h=50e-6, alpha_abs=0.2, alpha_sc=5e-5)
N = wg.N_reflections(100, np.radians(10))
P = wg.power(100, np.radians(10))

print(f"Reflections: {N:.2e}")
print(f"Power: {P:.4f}")
```

## 📊 Generate Paper Figures

```bash
python figures/generate_figures.py
```

## 📁 Project Structure

```
waveguide-reflection-framework/
├── src/
│   └── waveguide.py
├── figures/
│   └── generate_figures.py
├── examples/
│   └── example_usage.py
├── tests/
│   └── test_waveguide.py
├── requirements.txt
├── LICENSE
└── README.md
```

## 📝 Citation

```bibtex
@article{soltani2026waveguide,
  title={A Generalized Reflection-Count-Based Geometrical Optics Framework for Attenuation Analysis in Multimode Waveguides},
  author={Soltani, Abolfazl},
  journal={Journal of the Optical Society of America B},
  year={2026},
  note={Under review}
}
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

## 📧 Contact

Abolfazl Soltani - araz.soltani2007@gmail.com
