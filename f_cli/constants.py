"""f-cli constants."""

import os
from pathlib import Path

from f_lib import SystemInfo

__version__: str = "0.0.0"
"""Version of the Python package presented as a :class:`string`.

Dynamically set upon release by [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning).

"""

__version_tuple__: tuple[int, int, int] | tuple[int, int, int, str] = (0, 0, 0)
"""Version of the Python package presented as a :class:`tuple`.

Dynamically set upon release by [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning).

"""

SYSTEM_INFO = SystemInfo()
"""System information."""

CONFIG_DIR = (
    Path(os.environ["F_CLI_CONFIG_DIR"]).absolute()
    if os.getenv("F_CLI_CONFIG_DIR")
    else SYSTEM_INFO.os.user_config_dir / "finley"
)
