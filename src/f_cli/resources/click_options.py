"""Common click options."""
from typing import Callable

import functools

import click

# pylint: disable=invalid-name


DEBUG_HELP = ('Print all debug logs to the terminal. These logs WILL '
              'include credentials and secrets that should not shared.')
click_debug_option = click.option('--debug',
                                  is_flag=True,
                                  envvar='F_DEBUG',
                                  help=DEBUG_HELP)

VERBOSE_HELP = 'Print verbose logs to the terminal.'
click_verbose_option = click.option('--verbose',
                                    is_flag=True,
                                    envvar='F_VERBOSE',
                                    help=VERBOSE_HELP)


def click_common_options(command: Callable) -> Callable:
    """Decerator to add common options to click commands."""
    options = [click_debug_option, click_verbose_option]
    return functools.reduce(lambda x, opt: opt(x), options, command)
