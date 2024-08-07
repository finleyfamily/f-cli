"""Type definitions."""

from rich_click.rich_context import RichContext

from .context import Context


class ClickContext(RichContext):
    """Override ``rich_click.rich_context.RichContext`` to add a specific type for ``obj``."""

    obj: Context
    """Custom, persistant object."""
