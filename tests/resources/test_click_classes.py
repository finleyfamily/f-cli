"""Tests for src/f_cli/resources/click_classes.py."""
import json
from typing import List
from unittest import TestCase

import click
from click.testing import CliRunner, Result

from f_cli.resources.click_classes import CliGroup
from f_cli.resources.click_options import click_debug_option


class TestCliGroup(TestCase):
    """Tests for CliGroup"""

    runner: CliRunner = CliRunner()

    def test_args_as_context_object(self) -> None:
        """Ensure args saved as the context object."""
        args: List[str] = ['test_cmd', '--debug']

        @click.group('test_cli', cls=CliGroup)
        @click.pass_context
        def test_cli(ctx: click.Context) -> None:
            """A CLI for testing."""
            click.echo(json.dumps(ctx.obj))

        @test_cli.command('test_cmd')
        @click_debug_option
        def test_cmd(debug: bool) -> None:  # pylint: disable=unused-argument,unused-variable
            """A command for testing."""

        result: Result = self.runner.invoke(test_cli, args)
        output: List[str] = json.loads(result.output)

        self.assertEqual(output, args[1:])
