"""Context object."""
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from rich.console import Console

from .constants import CONFIG_DIR, SYSTEM_INFO

if TYPE_CHECKING:
    from pathlib import Path

    from f_lib import SystemInfo


class Context:
    """f-cli context object."""

    def __init__(self, *, console: Console | None = None) -> None:
        """Instantiate class."""
        self.console = console if console else Console()

    @cached_property
    def config_dir(self) -> Path:
        """Configuration directory.

        Upon first access, the directory and it's parents are created if they do not exist.

        """
        CONFIG_DIR.mkdir(exist_ok=True, parents=True)
        return CONFIG_DIR

    @property
    def sys(self) -> SystemInfo:
        """System information."""
        return SYSTEM_INFO


GLOBAL_CTX = Context()
"""Global context object.

The CLI needs a global context object that can be accessed outside of commands to generate some
commands. Adding it to :class:`f_lib.type_defs.ClickContext` is done for convenience.

"""
