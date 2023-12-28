"""Pytest configuration, fixtures, and plugins."""
from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from .factories import cli_runner_factory

if TYPE_CHECKING:
    from collections.abc import Iterator

    from _pytest.fixtures import SubRequest
    from click.testing import CliRunner


@pytest.fixture()
def cli_runner(request: SubRequest) -> CliRunner:
    """Initialize instance of `click.testing.CliRunner`."""
    return cli_runner_factory(request)


@pytest.fixture()
def cli_runner_isolated(cli_runner: CliRunner) -> Iterator[CliRunner]:
    """Initialize instance of :class:`click.testing.CliRunner` with ``isolate_filesystem()`` called."""
    with cli_runner.isolated_filesystem():
        yield cli_runner


@pytest.fixture()
def cd_tmp_path(tmp_path: Path) -> Iterator[Path]:
    """Change directory to a temporary path.

    Returns:
        Path: Temporary path object.

    """
    prev_dir = Path.cwd()
    os.chdir(tmp_path)
    try:
        yield tmp_path
    finally:
        os.chdir(prev_dir)
