#
#  This file is part of Sequana software
#
#  Copyright (c) 2016-2021 - Sequana Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/sequana/sequana
#  documentation: http://sequana.readthedocs.io
#
##############################################################################
import os
import sys

import rich_click as click
from sequana_pipetools import SequanaManager
from sequana_pipetools.options import *

NAME = "pacbio_qc"


help = init_click(
    NAME,
    groups={
        "Pipeline Specific": [
            "--do-kraken",
            "--kraken-databases",
        ],
    },
)


@click.command(context_settings=help)
@include_options_from(ClickSnakemakeOptions, working_directory=NAME)
@include_options_from(ClickSlurmOptions)
@include_options_from(ClickInputOptions, input_pattern="*.bam", add_input_readtag=False)
@include_options_from(ClickGeneralOptions)
@click.option(
    "--do-kraken",
    "do_kraken",
    is_flag=True,
    default=False,
    help="""If this option is set and valid DB are provided, run kraken taxonomy.""",
)
@click.option(
    "--kraken-databases",
    "kraken_databases",
    type=click.STRING,
    multiple=True,
    default=(),
    help="""Path to a valid set of Kraken database(s). If you do not have any,
         please see https://sequana.readthedocs.io or use sequana_taxonomy
         --download option. You may use several, in which case an iterative
         taxonomy is performed.""",
)
def main(**options):

    if options["from_project"]:
        click.echo("--from-project Not yet implemented")
        sys.exit(1)

    # the real stuff is here
    manager = SequanaManager(options, NAME)
    manager.setup()

    # aliases
    cfg = manager.config.config

    cfg.input_directory = os.path.abspath(options["input_directory"])
    cfg.input_pattern = options["input_pattern"]
    manager.exists(cfg.input_directory)

    # kraken
    cfg.kraken.do = bool(options["do_kraken"])

    if options["kraken_databases"]:
        cfg.kraken.databases = [os.path.abspath(x) for x in options["kraken_databases"]]
        for this in cfg.kraken.databases:
            manager.exists(this)
        cfg.kraken.do = True

    # finalise the command and save it; copy the snakemake. update the config
    # file and save it.
    manager.teardown()


if __name__ == "__main__":
    main()
