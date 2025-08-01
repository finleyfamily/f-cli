"""Custom patches."""

from __future__ import annotations

from typing import TYPE_CHECKING, Concatenate, ParamSpec, TypeVar

import click

if TYPE_CHECKING:
    from collections.abc import Callable

ClickContextTypeVar = TypeVar("ClickContextTypeVar", bound=click.Context)

P = ParamSpec("P")
R = TypeVar("R")


def pass_context[ClickContextTypeVar, **P, R](
    f: Callable[Concatenate[ClickContextTypeVar, P], R],
) -> Callable[P, R]:
    """Marks a callback as wanting to receive the current context object as first argument."""
    return click.pass_context(f)  # type: ignore[reportGeneralTypeIssues]
