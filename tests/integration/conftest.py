"""Pytest configuration, fixtures, and plugins."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from f_cli.context import GLOBAL_CTX

if TYPE_CHECKING:
    from pathlib import Path

    from pytest_mock import MockerFixture

    from f_cli.context import Context


@pytest.fixture(autouse=True)
def global_ctx(mocker: MockerFixture, tmp_path: Path) -> Context:
    """Patch the GLOBAL_CTX object."""
    config_dir = tmp_path / "finley"
    config_dir.mkdir()
    mocker.patch.object(GLOBAL_CTX, "config_dir", config_dir)
    return GLOBAL_CTX
