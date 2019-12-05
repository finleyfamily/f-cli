"""f-cli custom logging module."""
from typing import Any, Optional, TextIO, Union

from enum import IntEnum
import logging
import sys

import coloredlogs as cl

from f_cli import __version__

if sys.version_info[1] < 8:
    from typing_extensions import TypedDict  # noqa
else:
    from typing import TypedDict  # noqa pylint: disable=no-name-in-module,ungrouped-imports


LOG_FORMAT: str = '%(name)s: %(message)s'
LOG_FORMAT_W_LEVEL: str = '%(name)s: [%(levelname)s] %(message)s'
LOG_FIELD_STYLES: 'LogFieldStyles' = {
    'asctime': {
        'color': 'green'
    },
    'hostname': {
        'color': 'magenta'
    },
    'levelname': {
        'color': 'black',
        'bold': True
    },
    'name': {},
    'programname': {
        'color': 'cyan'
    }
}
LOG_LEVEL_STYLES: 'LogLevelStyles' = {
    'critical': {
        'color': 'red',
        'bold': True
    },
    'debug': {
        'color': 'green'
    },
    'error': {
        'color': 'red'
    },
    'info': {},
    'notice': {
        'color': 'magenta'
    },
    'spam': {
        'color': 'green',
        'faint': True
    },
    'success': {
        'color': 'green',
        'bold': True
    },
    'verbose': {
        'color': 'cyan'
    },
    'warning': {
        'color': 'yellow'
    }
}


class StylesAttribute(TypedDict, total=False):
    """Style attributes available for log fields and levels."""

    bold: Optional[bool]
    color: Optional[str]
    faint: Optional[bool]


class LogFieldStyles(TypedDict):
    """Style definitions for log fields."""

    asctime: StylesAttribute
    hostname: StylesAttribute
    levelname: StylesAttribute
    name: StylesAttribute
    programname: StylesAttribute


class LogLevelStyles(TypedDict):
    """Style definitions for log levels."""

    critical: StylesAttribute
    debug: StylesAttribute
    error: StylesAttribute
    info: StylesAttribute
    notice: StylesAttribute
    spam: StylesAttribute
    success: StylesAttribute
    verbose: StylesAttribute
    warning: StylesAttribute


class LogSettings(TypedDict):
    """Settings used to setup a logger."""

    stream: TextIO
    fmt: str
    field_styles: LogFieldStyles
    level_styles: LogLevelStyles


class LogLevels(IntEnum):
    """All available log levels."""

    NOTSET: int = 0
    DEBUG: int = 10
    VERBOSE: int = 15
    INFO: int = 20
    NOTICE: int = 25
    WARNING: int = 30
    SUCCESS: int = 35
    ERROR: int = 40
    CRITICAL: int = 50

    @classmethod
    def has_value(cls, value: int) -> bool:
        """Check if IntEnum has a value."""
        return value in cls._value2member_map_  # type: ignore  # pylint: disable=no-member


class FLogger(logging.Logger):
    """Extend built-in logger with additional levels."""

    def __init__(self, name: str, level: int = LogLevels.NOTSET) -> None:
        """Instantiate the class."""
        super().__init__(name, level)
        logging.addLevelName(LogLevels.VERBOSE, LogLevels.VERBOSE.name)
        logging.addLevelName(LogLevels.NOTICE, LogLevels.NOTICE.name)
        logging.addLevelName(LogLevels.SUCCESS, LogLevels.SUCCESS.name)

    def verbose(self, msg: Union[str, Exception], *args: Any, **kwargs: Any) -> None:
        """Log 'msg % args' with severity `VERBOSE`."""
        if self.isEnabledFor(LogLevels.VERBOSE):
            self._log(LogLevels.VERBOSE, msg, args, **kwargs)  # type: ignore

    def notice(self, msg: Union[str, Exception], *args: Any, **kwargs: Any) -> None:
        """Log 'msg % args' with severity `NOTICE`."""
        if self.isEnabledFor(LogLevels.NOTICE):
            self._log(LogLevels.NOTICE, msg, args, **kwargs)  # type: ignore

    def success(self, msg: Union[str, Exception], *args: Any, **kwargs: Any) -> None:
        """Log 'msg % args' with severity `SUCCESS`."""
        if self.isEnabledFor(LogLevels.SUCCESS):
            self._log(LogLevels.SUCCESS, msg, args, **kwargs)  # type: ignore


def setup_logging(level: int = LogLevels.INFO) -> None:
    """Configure log settings.

    It is recommended to use a level of INFO or lower so that important
    information is not lost.

    When the level is set to debug, additional dependance logs will be
    shown.

    Args:
        level: The level of logs that will be displayed. This should not
            be set higher then INFO.

    """
    level_for_dependencies = (LogLevels.WARNING
                              if level >= LogLevels.VERBOSE else level)
    logging.setLoggerClass(FLogger)

    log_settings: LogSettings = {
        'stream': sys.stderr,
        'fmt': LOG_FORMAT,
        'field_styles': LOG_FIELD_STYLES,
        'level_styles': LOG_LEVEL_STYLES
    }

    logging.disable(LogLevels.NOTSET)

    f_logger: logging.Logger = logging.getLogger('f-cli')
    boto3_logger: logging.Logger = logging.getLogger('boto3')
    botocore_logger: logging.Logger = logging.getLogger('botocore')

    cl.install(level, logger=f_logger, **log_settings)

    cl.install(level_for_dependencies, logger=boto3_logger,
               **log_settings)
    cl.install(level_for_dependencies, logger=botocore_logger,
               **log_settings)

    f_logger.debug('Initalized logging for f-cli version %s',
                   __version__)
