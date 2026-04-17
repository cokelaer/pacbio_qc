

.. image:: https://badge.fury.io/py/sequana-pacbio-qc.svg
     :target: https://pypi.python.org/pypi/sequana_pacbio_qc

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
    :target: http://joss.theoj.org/papers/10.21105/joss.00352
    :alt: JOSS (journal of open source software) DOI

.. image:: https://github.com/sequana/pacbio_qc/actions/workflows/main.yml/badge.svg
   :target: https://github.com/sequana/pacbio_qc/actions/workflows    

.. image:: https://img.shields.io/badge/python-3.11%20%7C%203.12-blue.svg
    :target: https://pypi.python.org/pypi/sequana_pacbio_qc
    :alt: Python 3.11 | 3.12


This is the **pacbio_qc** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ project

:Overview: Quality control and analysis for PacBio long-read sequencing data (BAM files). Generates comprehensive statistics on read quality, length distribution, and GC content, with optional taxonomic classification.

:Input: BAM files from PacBio sequencers (raw subreads, CCS, or processed reads)
:Output: Per-sample HTML reports with interactive visualizations, quality metrics, and optional taxonomic classification; comprehensive summary report with all samples
:Status: production
:Documentation: This README file, the Wiki from the github repository (link above) and https://sequana.readthedocs.io
:Citation: Cokelaer et al, (2017), ‘Sequana’: a Set of Snakemake NGS pipelines, Journal of Open Source Software, 2(16), 352, JOSS DOI doi:10.21105/joss.00352


Installation
~~~~~~~~~~~~

Install via pip::

    pip install sequana_pacbio_qc

**Optional dependencies:**

- **kraken2**: For taxonomic classification (optional, disabled by default)
- **graphviz**: For DAG visualization
- **apptainer**: For containerized execution of tools


Quick Start
~~~~~~~~~~~

::

    # Display help
    sequana_pacbio_qc --help

    # Create pipeline in current directory
    sequana_pacbio_qc --input-directory /path/to/bam/files

    # With optional Kraken taxonomy
    sequana_pacbio_qc --input-directory /path/to/bam/files --do-kraken --kraken-databases /path/to/kraken/db

    # Using apptainer containers
    sequana_pacbio_qc --input-directory /path/to/bam/files --apptainer-prefix ~/containers

This creates a ``pacbio_qc`` directory containing the pipeline and configuration files.


Execution
~~~~~~~~~

Execute the pipeline::

    cd pacbio_qc
    bash pacbio_qc.sh

Or with custom Snakemake parameters::

    snakemake -s pacbio_qc.rules -c config.yaml --cores 4 --stats stats.txt

Or use the `sequanix <https://sequana.readthedocs.io/en/master/sequanix.html>`_ graphical interface.


Configuration
~~~~~~~~~~~~~

The pipeline uses ``config.yaml`` to control:

- **Input data**: BAM file directory and pattern matching
- **Kraken**: Optional taxonomic database paths (disabled by default)
- **MultiQC**: QC report options
- **Apptainer**: Container image URLs (optional)

Pipeline Overview
~~~~~~~~~~~~~~~~~~

.. image:: https://raw.githubusercontent.com/sequana/pacbio_qc/master/sequana_pipelines/pacbio_qc/dag.png


Workflow Details
~~~~~~~~~~~~~~~~

The pipeline performs the following analyses on PacBio BAM files:

1. **Quality Metrics**: Computes read length statistics, GC content distribution, and signal-to-noise ratios
2. **Visualizations**: Generates histograms and scatter plots for quality assessment
3. **Per-Sample Reports**: Creates individual HTML reports for each sample with:

   - Read length distribution histograms
   - GC content analysis
   - SNR (signal-to-noise ratio) metrics
   - Quality overview with sample statistics

4. **Taxonomy (Optional)**: Performs taxonomic classification using Kraken2 when enabled
5. **Summary Report**: Generates a comprehensive HTML summary with:

   - Overview of pipeline and all samples
   - Summary statistics table with links to per-sample reports
   - MultiQC aggregated quality metrics

**Note:** Kraken2 databases are not provided with the pipeline. This step is optional and disabled by default.


Changelog
~~~~~~~~~
========= ====================================================================
Version   Description
========= ====================================================================
1.0.1     HTML reports with pipeline overview; race condition handling for
          parallel execution with --apptainer-prefix; improved CI/CD workflows
1.0.0     Uses latest wrappers and graphviz apptainers
0.11.0    Release to use latests sequana_pipetools framework
0.10.0    Update to use latest tools from sequana framework
0.9.0     First release of sequana_pacbio_qc using latest sequana rules and
          modules (0.9.5)
========= ====================================================================


Contribute & Code of Conduct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To contribute to this project, please take a look at the 
`Contributing Guidelines <https://github.com/sequana/sequana/blob/main/CONTRIBUTING.rst>`_ first. Please note that this project is released with a 
`Code of Conduct <https://github.com/sequana/sequana/blob/main/CONDUCT.md>`_. By contributing to this project, you agree to abide by its terms.


Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the `latest documented configuration file <https://raw.githubusercontent.com/sequana/sequana_pacbio_qc/main/sequana_pipelines/pacbio_qc/config.yaml>`_
to be used with the pipeline. Each rule used in the pipeline may have a section in the configuration file. 



.. |Codacy-Grade| image:: https://app.codacy.com/project/badge/Grade/9b8355ff642f4de9acd4b270f8d14d10
   :target: https://www.codacy.com/gh/sequana/pacbio_qc/dashboard

