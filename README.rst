========================================================================
ChemLearn: Deep neural networks for chemistry
========================================================================

|Version| |License| |PyPI| |Docs| |DOI| |Tweet|

.. |Version| image:: https://img.shields.io/badge/python-3.7%2B-green.svg
  :target: https://www.python.org/

.. |License| image:: https://img.shields.io/github/license/mashape/apistatus.svg
  :target: https://github.com/SanjeevaRDodlapati/Chem-Learn/tree/master/LICENSE

.. |PyPI| image:: https://img.shields.io/badge/pypi-latest-orange.svg
  :target: https://pypi.python.org/pypi/chemlearn

.. |Docs| image:: https://img.shields.io/badge/docs-up--to--date-brightgreen.svg
  :target: http://chemlearn.readthedocs.io

.. |DOI| image:: https://zenodo.org/badge/68630079.svg
   :target: https://zenodo.org/badge/latestdoi/68630079

.. |Tweet| image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social
  :target: https://twitter.com/intent/tweet?text=Checkout+%23DeepCpG%3A+%23DeepLearning+for+predicting+DNA+methylation%2C+%40cangermueller

DeepCpG [1]_ is a deep neural network for predicting the methylation state of CpG dinucleotides in multiple cells. It allows to accurately impute incomplete DNA methylation profiles, to discover predictive sequence motifs, and to quantify the effect of sequence mutations. (`Angermueller et al, 2017 <http://dx.doi.org/10.1186/s13059-017-1189-z>`_).

**Please help to improve DeepCpG**, by reporting bugs, typos in notebooks and documentation, or any ideas on how to make things better. You can submit an `issue <https://github.com/cangermueller/deepcpg/issues>`_ or send me an `email <mailto:cangermueller@gmail.com>`_.

.. figure:: docs/source/fig1.png
   :width: 640 px
   :align: left
   :alt: DeepCpG model architecture and applications

   **DeepCpG model architecture and applications.**

   \(a\) Sparse single-cell CpG profiles as obtained from scBS-seq or scRRBS-seq. Methylated CpG sites are denoted by ones, unmethylated CpG sites by zeros, and question marks denote CpG sites with unknown methylation state (missing data). (b) DeepCpG model architecture. The DNA model consists of two convolutional and pooling layers to identify predictive motifs from the local sequence context, and one fully connected layer to model motif interactions. The CpG model scans the CpG neighborhood of multiple cells (rows in b), using a bidirectional gated recurrent network (GRU), yielding compressed features in a vector of constant size. The Joint model learns interactions between higher-level features derived from the DNA- and CpG model to predict methylation states in all cells. (c, d) The trained DeepCpG model can be used for different downstream analyses, including genome-wide imputation of missing CpG sites (c) and the discovery of DNA sequence motifs that are associated with DNA methylation levels or cell-to-cell variability (d).


.. [1] Angermueller, Christof, Heather J. Lee, Wolf Reik, and Oliver Stegle. *DeepCpG: Accurate Prediction of Single-Cell DNA Methylation States Using Deep Learning.* Genome Biology 18 (April 11, 2017): 67. doi:10.1186/s13059-017-1189-z.


Table of contents
=================
* `News`_
* `Installation`_
* `Getting started`_
* `Examples`_
* `Model Zoo`_
* `FAQ`_
* `Content`_
* `Changelog`_
* `Contact`_


News
====

* **181201**: DeepCpG 1.0.7 released!
* **180224**: DeepCpG 1.0.6 released!
* **171112**: Keras 2 is now the main Keras version (release 1.0.5).
* **170412**: New `notebook <./examples/notebooks/stats/index.ipynb>`_ on predicting inter-cell statistics!
* **170414**: Added `dcpg_eval_perf.py <./scripts/dcpg_eval_perf.py>`_ and `dcpg_eval_perf.Rmd <./R/dcpg_eval_perf.Rmd>`_ for evaluating and visualizing prediction performances! Find an example in `this notebook <./examples/notebooks/basics/index.ipynb#Evaluating-prediction-performances>`_!
* **170412**: New `notebook <./examples/notebooks/stats/index.ipynb>`_ on predicting inter-cell statistics!
* **170410**: New `notebook <./examples/notebooks/snp/index.ipynb>`_ on estimating mutation effects!
* **170406**: A short description of all `DeepCpG scripts <http://deepcpg.readthedocs.io/latest/scripts/index.html>`_!
* **170404**: New guide on creating and analyzing DeepCpG data `released <http://deepcpg.readthedocs.io/latest/data.html>`_!
* **170404**: Training on continuous data, e.g. from bulk experiments, now `supported <http://deepcpg.readthedocs.io/latest/data.html>`_!


Installation
============

The easiest way to install DeepCpG is to use ``PyPI``:

.. code:: bash

  pip install deepcpg

Alternatively, you can checkout the repository,

.. code:: bash

  git clone https://github.com/cangermueller/deepcpg.git


and then install DeepCpG using ``setup.py``:

.. code:: bash

  python setup.py install


Getting started
===============

1. Store known CpG methylation states of each cell into a tab-delimted file with the following columns:

* Chromosome (without chr)
* Position of the CpG site on the chromosome starting with one
* Binary methylation state of the CpG sites (0=unmethylation, 1=methylated)
