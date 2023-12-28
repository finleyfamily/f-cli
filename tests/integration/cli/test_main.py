"""Test f_cli._cli.main."""
from __future__ import annotations

from typing import TYPE_CHECKING

from f_cli._cli import cli
from f_cli.constants import __version__

if TYPE_CHECKING:
    from click.testing import CliRunner

MODULE = "f_cli._cli.main"


def test_version(cli_runner: CliRunner) -> None:
    """Test ``f --version``."""
    result = cli_runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert result.stdout == f"{__version__}\n"
