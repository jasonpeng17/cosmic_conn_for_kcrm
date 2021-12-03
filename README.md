# Cosmic-CoNN
## A Cosmic Ray Detection Deep Learning Framework, Dataset, and Toolkit

[Github](https://github.com/cy-xu/cosmic-conn) • [Quick Start](https://github.com/cy-xu/cosmic-conn#Installation) • [Publication](https://github.com/cy-xu/cosmic-conn#publication) • [PyPI Release](https://pypi.org/project/cosmic-conn/) • [Documentation](https://cosmic-conn.readthedocs.io/) • [LCO CR Dataset](https://zenodo.org/record/5034763)

[![arXiv](https://img.shields.io/badge/arXiv-2106.14922-b31b1b.svg?style=flat)](https://arxiv.org/abs/2106.14922) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5034763.svg)](https://doi.org/10.5281/zenodo.5034763) [![PyPI version](https://badge.fury.io/py/cosmic-conn.svg)](https://badge.fury.io/py/cosmic-conn) [![readthedocs](https://readthedocs.org/projects/cosmic-conn/badge/?version=latest)](https://cosmic-conn.readthedocs.io) [![astropy](http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat)](http://www.astropy.org/) [![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg?style=flat-square)](https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3))

## About 
![Cosmic-CoNN overview](https://cosmic-conn.readthedocs.io/en/latest/_images/Cosmic-CoNN_overview.png)

Cosmic-CoNN is an end-to-end solution to help tackle the cosmic ray (CR) detection problem in CCD-captured astronomical images. It includes a deep-learning framework, high-performance CR detection models, a new dataset, and a suite of tools to use to the models, shown in the figure above:

1. [LCO CR dataset](https://zenodo.org/record/5034763), a large, diverse cosmic ray dataset  consists of over 4,500 scientific images from [Las Cumbres Observatory](https://lco.global/) (LCO) global telescope network's 23 instruments. CRs are labeled accurately and consistently across many diverse observations from various instruments. To the best of our knowledge, this is the largest dataset of its kind. 

2. A PyTorch deep-learning framework that trains generic, robust CR detection models for ground- and space-based imaging data, as well as spectroscopic observations.

3. A suite of tools includinging console commands, a web app, and Python APIs to make deep-learning models easily accessible to astronomers.

![Detection demo on Gemini data](https://cosmic-conn.readthedocs.io/en/latest/_images/fig11_gemini_results_demo.png)
Visual inspection of Cosmic-CoNNCR detection results. Detecting CRs in a Gemini GMOS-N 1×1 binning image with our generic ``ground-imaging`` model. The model was trained entirely on LCO data yet all visible CRs in the image stamp are correctly detected regardless of their shapes or sizes.

![Detection demo on LCO NRES data](https://cosmic-conn.readthedocs.io/en/latest/_images/fig11_nres_result_0034_1.png)
The Cosmic-CoNN ``NRES`` model detects CRs over the spectrum robustly on a LCO NRES spectroscopic image. The horizontal bands in the left image are the spectroscopicorders, which are left out of the CR mask.

## Publication

<p>
<a href="https://arxiv.org/abs/2106.14922"><img style="float: left; padding-right:30px;" src="https://cosmic-conn.readthedocs.io/en/latest/_images/paper_with_shadow.png"  width="220"/></a>

This repository is part of our Cosmic-CoNN research paper. Our methods and a thorough evaluation of models' performance are available in the paper. If you used the Cosmic-CoNN or the LCO CR dataset for your research, pleaes cite our paper:

[arXiv:2106.14922](https://arxiv.org/abs/2106.14922), [NASA ADS](https://ui.adsabs.harvard.edu/abs/2021arXiv210614922X/abstract)

Please also cite the LCO CR datset if you used the Cosmic-CoNN `ground_imaging` model or the data in your research:

Xu, Chengyuan, McCully, Curtis, Dong, Boning, Howell, D. Andrew, & Sen, Pradeep. (2021). Cosmic-CoNN LCO CR Dataset (Version 0.1.0) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.5034763

</p>

<br/><br/>
## Installation

*We recently added optional dependencies install for pip.*

We recommend installing Cosmic-CoNN in a new virutal enviroment, see the step-by-step [installation guide](https://cosmic-conn.readthedocs.io/en/latest/source/installation.html). To get a ~10x speed-up with GPU acceleration, see [Install for a CUDA-enabled GPU](https://cosmic-conn.readthedocs.io/en/latest/source/installation.html).

```console
  # basic install for CR detection or library integration
  $ pip install cosmic-conn

  # include Flask for the web app interface
  $ pip install cosmic-conn[webapp] 

  # install all dependencies for development
  $ pip install cosmic-conn[develop] 
```

## Command line interface

After installation, you can start CR detection in FITS files right from the terminal:

```console
  $ cosmic-conn -m ground_imaging -e SCI -i input_dir
```

This command launches a generic `gorund_imaging` model to detect cosmic rays. It reads data from the SCI extention in a FITS file and process all files in the input_dir. We also provide the `NRES` model for CR detection in spectroscopic data and the `HST_ACS_WFC` model for Hubble ACS/WFC imaging data. You could also find more Hubble Space Telescope CR detection and inpainting models trained by [deepCR](https://github.com/profjsb/deepCR).

See [documentation](https://cosmic-conn.readthedocs.io/en/latest/source/user_guide.html) for the complete user guide.

## Python APIs

It is also easy to integrate Cosmic-CoNN CR detection into your data workflow. Let `image` be a two-dimensional `float32 numpy` array of any size:

```Python

  from cosmic_conn import init_model

  # initialize a Cosmic-CoNN model
  cr_model = init_model("ground_imaging")

  # the model outputs a CR probability map in np.float32
  cr_prob = cr_model.detect_cr(image)

  # convert the probability map to a boolean mask with a 0.5 threshold
  cr_mask = cr_prob > 0.5

```

## Web app

```console
  $ cosmic-conn -a ground_imaging -e SCI
```

The Cosmic-CoNN web app automatically finds large CRs for close inspection. It supports live CR mask editing and is especially useful to find the suitable thresholds for different types of observations:

<img src="https://cosmic-conn.readthedocs.io/en/latest/_images/cosmic_conn_web_app_interface.png" alt="web-based CR detector interface" width="600"/>

The Cosmic-CoNN web app interface.

## Train new models with Cosmic-CoNN

See [documentation](https://cosmic-conn.readthedocs.io/en/latest/source/lco_cr_dataset.html) for the developler guide on using LCO CR dataset, data reduction, and model training.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
