"""f-cli constants."""
import os
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from f_lib import SystemInfo

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # cov: ignore
    # package is not installed
    __version__ = "0.0.0"

SYSTEM_INFO = SystemInfo()
"""System information."""

CONFIG_DIR = (
    Path(os.environ["F_CLI_CONFIG_DIR"]).absolute()
    if os.getenv("F_CLI_CONFIG_DIR")
    else SYSTEM_INFO.os.user_config_dir / "finley"
)
