"""f-cli entrypoint."""
from typing import Any, Dict, List, Optional, Union
import sys

import click

from . import __version__


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


@click.group(context_settings=CLICK_CONTEXT_SETTINGS)
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def cli() -> None:
    """f-cli tool."""


def main() -> int:
    """CLI entrypoint."""
    try:
        cli.main(prog_name='f')
    except Exception:  # pylint: disable=broad-except
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
