"""f-cli context object."""
from typing import cast

import logging

from click import Context as ClickContext

from .base import BaseClass
from .logging import FLogger
from .resources.user import User


logging.setLoggerClass(FLogger)
LOG = cast(FLogger, logging.getLogger('f-cli'))


class ContextObject(BaseClass):  # TODO determine the other attributes needed here
    """f-cli context object."""

    log = LOG
    repo_url: str = 'https://github.com/ITProKyle/f-cli'
    user: User

    def __init__(self) -> None:
        """Initialize class."""
        self.user = User()  # TODO update when the user needs args


class Context(ClickContext):
    """Extends click.Context for type annotations."""

    obj: ContextObject
