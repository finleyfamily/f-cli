"""CLI commands for interacting with the CLI's configuration."""

import rich_click as click

from ._init import self_config_init

COMMANDS = [self_config_init]


@click.group("config")
def self_config() -> None:
    """CLI commands for interacting with the CLI's configuration."""


for cmd in COMMANDS:  # register commands
    self_config.add_command(cmd)
