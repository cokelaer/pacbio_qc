import os
import subprocess
import sys
import tempfile

from click.testing import CliRunner

from sequana_pipelines.pacbio_qc.main import main

from . import test_dir

sharedir = f"{test_dir}/data"


def test_standalone_subprocess():
    directory = tempfile.TemporaryDirectory()
    cmd = [
        "sequana_pacbio_qc",
        "--input-directory", sharedir,
        "--working-directory", directory.name,
        "--force",
    ]
    subprocess.call(cmd)


def test_standalone_script():
    directory = tempfile.TemporaryDirectory()
    runner = CliRunner()
    results = runner.invoke(
        main,
        [
            "--input-directory", sharedir,
            "--working-directory", directory.name,
            "--force",
        ],
    )
    assert results.exit_code == 0


def test_full1():
    with tempfile.TemporaryDirectory() as directory:
        wk = directory
        runner = CliRunner()
        results = runner.invoke(
            main,
            [
                "--input-directory", sharedir,
                "--working-directory", wk,
                "--force",
            ],
        )
        assert results.exit_code == 0

        stat = subprocess.call(["bash", "pacbio_qc.sh"], cwd=wk)
        assert os.path.exists(wk + "/multiqc/multiqc_report.html")


def test_full2():
    with tempfile.TemporaryDirectory() as directory:
        wk = directory
        database = f"{sharedir}/toydb"
        runner = CliRunner()
        results = runner.invoke(
            main,
            [
                "--input-directory", sharedir,
                "--working-directory", wk,
                "--force",
                "--do-kraken",
                "--kraken-databases", database,
            ],
        )
        assert results.exit_code == 0

        stat = subprocess.call(["bash", "pacbio_qc.sh"], cwd=wk)
        assert os.path.exists(wk + "/multiqc/multiqc_report.html")


def test_version():
    cmd = ["sequana_pacbio_qc", "--version"]
    subprocess.call(cmd)
