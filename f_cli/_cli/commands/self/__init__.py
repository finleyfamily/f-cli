"""CLI commands for interacting with the CLI itself."""

import rich_click as click

from .config import self_config

COMMANDS = [self_config]


@click.group()
def self() -> None:
    """CLI commands for interacting with the CLI itself."""


for cmd in COMMANDS:  # register commands
    self.add_command(cmd)
