"""f-cli user."""
from typing import Any, Dict

from ..base import BaseClass


class User(BaseClass):  # TODO add attributes - still need to figure out what is needed
    """f-cli user."""

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        """Initialize class."""
