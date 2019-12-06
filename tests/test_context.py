"""Tests for src/f_cli/context.py."""
import logging
from unittest import TestCase

from f_cli.context import ContextObject
from f_cli.resources.user import User


class TestContext(TestCase):
    """Tests for Context."""

    def test_attributes(self) -> None:
        """Just need any test right now. The class does nothing yet."""
        ctx = ContextObject()

        self.assertIsInstance(ctx.log, logging.Logger)
        self.assertEqual(ctx.repo_url,
                         'https://github.com/ITProKyle/f-cli')
        self.assertIsInstance(ctx.user, User)
