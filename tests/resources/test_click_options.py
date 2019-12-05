"""Tests for src/f_cli/resources/click_options.py."""
from typing import Any, Dict

import json
from unittest import TestCase

import click
from click.testing import CliRunner, Result

from f_cli.resources.click_options import (click_common_options,
                                           click_debug_option,
                                           click_verbose_option)


class TestSingleOptions(TestCase):
    """Test for single options."""

    runner: CliRunner = CliRunner()

    def test_click_debug_option(self) -> None:
        """Tests for the debug option."""
        @click.command('test_func')
        @click_debug_option
        def test_func(debug: bool) -> None:
            """Function for testing options."""
            click.echo(debug)

        default_result: Result = self.runner.invoke(test_func, [])
        flag_result: Result = self.runner.invoke(test_func,
                                                 args=['--debug'])
        envvar_result: Result = self.runner.invoke(test_func, env={'F_DEBUG': '1'})

        self.assertEqual(default_result.output, 'False\n',
                         'output should be `False` when flag is not '
                         'present')
        self.assertEqual(flag_result.output, 'True\n',
                         'output should be `True` when flag is '
                         'present')
        self.assertEqual(envvar_result.output, 'True\n',
                         'output should be `True` when flag is not'
                         'present but env var is set')

    def test_click_verbose_option(self) -> None:
        """Tests for the verbose option."""
        @click.command('test_func')
        @click_verbose_option
        def test_func(verbose: bool) -> None:
            """Function for testing options."""
            click.echo(verbose)

        default_result: Result = self.runner.invoke(test_func, [])
        flag_result: Result = self.runner.invoke(test_func,
                                                 args=['--verbose'])
        envvar_result: Result = self.runner.invoke(test_func, env={'F_VERBOSE': '1'})

        self.assertEqual(default_result.output, 'False\n',
                         'output should be `False` when flag is not '
                         'present')
        self.assertEqual(flag_result.output, 'True\n',
                         'output should be `True` when flag is '
                         'present')
        self.assertEqual(envvar_result.output, 'True\n',
                         'output should be `True` when flag is not'
                         'present but env var is set')


class TestMultipleOptionDecorators(TestCase):
    """Test for single options."""

    runner: CliRunner = CliRunner()

    def test_click_common_options(self) -> None:
        """Tests for common options wrapper."""
        args = ['--debug', '--verbose']

        @click.command('test_func')
        @click_common_options
        def test_func(**kwargs: Dict[str, Any]) -> None:
            """Function for testing options."""
            click.echo(json.dumps(kwargs))

        result = json.loads(
            self.runner.invoke(test_func, args).output.replace('\n', '')
        )

        self.assertEqual(result, {'debug': True, 'verbose': True})
