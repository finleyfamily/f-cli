"""f-cli entrypint."""
from __future__ import annotations

from typing import TYPE_CHECKING

import rich_click as click

from ..constants import __version__
from ..context import Context
from ._patch import pass_context

if TYPE_CHECKING:
    from ..type_defs import ClickContext

CLICK_CONTEXT_SETTINGS: dict[str, object] = {
    "help_option_names": ["-h", "--help"],
    "max_content_width": 100,
}

click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.MAX_WIDTH = 100
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.USE_RICH_MARKUP = True


@click.group(context_settings=CLICK_CONTEXT_SETTINGS)
@click.version_option(__version__, message="%(version)s")
@pass_context
def cli(ctx: ClickContext) -> None:
    """Finley CLI."""
    ctx.obj = Context()
