"""Test f_cli._cli.commands.self.config._init."""
from __future__ import annotations

from typing import TYPE_CHECKING

from f_cli._cli import cli

if TYPE_CHECKING:
    from click.testing import CliRunner

    from f_cli.context import Context


def test_init(cli_runner: CliRunner, global_ctx: Context) -> None:
    """Test init."""
    result = cli_runner.invoke(cli, ["self", "config", "init"])
    assert result.exit_code == 0
    assert f"created in {global_ctx.config_dir}" in result.stdout.replace("\n", "")
