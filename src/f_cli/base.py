"""Base classes used for some objects."""
from collections.abc import MutableMapping
from typing import Any, Dict, Iterator


class BaseClass(MutableMapping):
    """A base class for mutable map like objects."""

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        """Initialize class.

        Provided ``kwargs`` are added to the object as attributes.

        Example:
            .. codeblock: python

                obj = Baseclass(**{'key': 'value'})
                print(obj.__dict__)
                # {'key': 'value'}

        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, key: str) -> Any:
        """Implement evaluation of self[key].

        Args:
            key: Attribute name to return the value for.

        Returns:
            The value associated with the provided key/attribute name.

        Raises:
            Attribute: If attribute does not exist on this object.

        Example:
            .. codeblock: python

                obj = Baseclass(**{'key': 'value'})
                print(obj['key'])
                # value

        """
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        """Implement assignment to self[key].

        Args:
            key: Attribute name to associate with a value.
            value: Value of a key/attribute.

        Example:
            .. codeblock: python

                obj = Baseclass()
                obj['key'] = 'value'
                print(obj['key'])
                # value

        """
        setattr(self, key, value)

    def __delitem__(self, key: str) -> None:
        """Implement deletion of self[key].

        Args:
            key: Attribute name to remove from the object.

        Example:
            .. codeblock: python

                obj = Baseclass(**{'key': 'value'})
                del obj['key']
                print(obj.__dict__)
                # {}

        """
        delattr(self, key)

    def __len__(self) -> int:
        """Implement the built-in function len().

        Example:
            >>> obj = Baseclass(**{'key': 'value'})
            ... print(len(obj))
            1

        """
        return len(self.__dict__)

    def __iter__(self) -> Iterator[Any]:
        """Return iterator object that can iterate over all attributes.

        Example:
            .. codeblock: python

                obj = Baseclass(**{'key': 'value'})
                for k, v in obj.items():
                    print(f'{key}: {value}')
                # key: value

        """
        return iter(self.__dict__)
