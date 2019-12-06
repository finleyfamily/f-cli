"""Tests for src/f_cli/base.py."""
from collections.abc import ItemsView
from unittest import TestCase

from f_cli.base import BaseClass


class TestBaseClass(TestCase):
    """Tests for BaseClass."""

    def test_init(self) -> None:
        """Ensure attributes are added."""
        expected = {'key': 'value'}

        obj = BaseClass(**expected)

        self.assertEqual(obj.__dict__, expected)

        obj = BaseClass(key='value')

        self.assertEqual(obj.__dict__, expected)

    def test_getitem(self) -> None:
        """Ensure attribute value is returned using bracket notation."""
        obj = BaseClass(**{'key': 'value'})

        self.assertEqual(obj['key'], 'value')

    def test_getitem_keyerror(self) -> None:
        """Raise KeyError when attribute does not exist."""
        obj = BaseClass()

        with self.assertRaises(AttributeError):
            print(obj['key'])

    def test_setitem(self) -> None:
        """Ensure attribute is added to the object."""
        obj = BaseClass()
        obj['key'] = 'value'

        self.assertEqual(obj['key'], 'value')

    def test_delitem(self) -> None:
        """Ensure attribute is removed from the object."""
        obj = BaseClass(**{'key': 'value'})
        del obj['key']

        with self.assertRaises(AttributeError):
            print(obj['key'])

    def test_len(self) -> None:
        """Ensure len() calls __len__ for the correct value."""
        obj = BaseClass(**{'key': 'value'})

        self.assertEqual(len(obj), 1)

    def test_iter(self) -> None:
        """Ensure object is iterable."""
        obj = BaseClass(**{'key': 'value'})

        self.assertIsInstance(obj.items(), ItemsView)
