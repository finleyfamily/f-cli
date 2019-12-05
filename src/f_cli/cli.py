"""f-cli entrypoint."""
from typing import Any, Dict, List, Optional, Tuple, Union

import sys

import click

from . import __version__
from .logging import LogLevels, setup_logging
from .resources.click_classes import CliGroup
from .resources.click_options import click_common_options


CLICK_CONTEXT_SETTINGS: Dict[str, Union[int, List[str]]] = {
    'help_option_names': ['-h', '--help'],
    'max_content_width': 999
}


def print_version(ctx: Optional[click.Context],
                  _param: Optional[Union[click.Parameter, click.Option]],
                  value: Any
                  ) -> None:
    """Display f-cli version then exit.

    Args:
        ctx: Click context only used to exit the command.
        param: Not used.
        value: Not used.

    """
    if not value or not ctx or ctx.resilient_parsing:
        return
    click.echo(f'f-cli version {__version__}')
    ctx.exit()


@click.group(context_settings=CLICK_CONTEXT_SETTINGS, cls=CliGroup)
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click_common_options
@click.pass_context
def cli(ctx: click.Context,
        debug: bool = False,
        verbose: bool = False) -> None:
    """f-cli tool."""
    args: Tuple[str, ...] = getattr(ctx.obj, 'args', ctx.obj)

    if debug or '--debug' in args:
        setup_logging(LogLevels.DEBUG)
    elif verbose or '--verbose' in args:
        setup_logging(LogLevels.VERBOSE)
    else:
        setup_logging(LogLevels.INFO)


def main() -> int:
    """CLI entrypoint."""
    try:
        cli.main(prog_name='f')
    except Exception:  # pylint: disable=broad-except
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
