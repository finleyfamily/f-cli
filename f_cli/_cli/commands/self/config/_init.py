"""Initiate the CLI's configuration files."""

from __future__ import annotations

from typing import TYPE_CHECKING

import rich_click as click

from f_cli._cli._patch import pass_context

if TYPE_CHECKING:
    from f_cli.type_defs import ClickContext


@click.command("init")
@pass_context
def self_config_init(ctx: ClickContext) -> None:
    """Initiate the CLI's configuration files."""
    ctx.obj.console.print("Welcome to f-cli!")
    ctx.obj.console.print(f"Configuration files will now be created in {ctx.obj.config_dir}...")
    ctx.obj.console.print("[bold green]Configuration files have successfully been created![/]")
