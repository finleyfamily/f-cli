"""Custom patches."""

from __future__ import annotations

from typing import TYPE_CHECKING, Concatenate, ParamSpec, TypeVar

import click

if TYPE_CHECKING:
    from collections.abc import Callable

_ClickContextTypeVar = TypeVar("_ClickContextTypeVar", bound=click.Context)

_P = ParamSpec("_P")
_R = TypeVar("_R")


def pass_context(
    f: Callable[Concatenate[_ClickContextTypeVar, _P], _R]
) -> Callable[_P, _R]:
    """Marks a callback as wanting to receive the current context object as first argument."""
    return click.pass_context(f)  # type: ignore[reportGeneralTypeIssues]
