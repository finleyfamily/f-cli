"""Factories for tests."""
from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, cast

from click.testing import CliRunner

if TYPE_CHECKING:
    import pytest
    from _pytest.fixtures import SubRequest


def cli_runner_factory(request: SubRequest) -> CliRunner:
    """Initialize instance of `click.testing.CliRunner`."""
    kwargs: dict[str, Any] = {"env": os.environ.copy()}
    mark = cast("pytest.Mark | None", request.node.get_closest_marker("cli_runner"))
    if mark:
        kwargs.update(cast(dict[str, Any], mark.kwargs))
    return CliRunner(**kwargs)
