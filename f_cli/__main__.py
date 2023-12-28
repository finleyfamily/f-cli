"""Implement invoking f-cli as ``python -m f_cli``."""
import sys

from ._cli.main import cli

sys.exit(cli())
