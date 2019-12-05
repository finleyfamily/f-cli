"""Tests for src/f_cli/logging.py."""
import logging
from unittest import TestCase

from f_cli import __version__
from f_cli.logging import FLogger, LogLevels, setup_logging

logging.setLoggerClass(FLogger)


class TestLogLevels(TestCase):
    """Test for LogLevels."""

    def test_level_values(self) -> None:
        """Ensure levels have the appropriate values."""
        self.assertEqual(LogLevels.NOTSET, 0)
        self.assertEqual(LogLevels.DEBUG, 10)
        self.assertEqual(LogLevels.VERBOSE, 15)
        self.assertEqual(LogLevels.INFO, 20)
        self.assertEqual(LogLevels.NOTICE, 25)
        self.assertEqual(LogLevels.WARNING, 30)
        self.assertEqual(LogLevels.SUCCESS, 35)
        self.assertEqual(LogLevels.ERROR, 40)
        self.assertEqual(LogLevels.CRITICAL, 50)

    def test_has_value(self) -> None:
        """Ensure has_value can validate all values."""
        self.assertTrue(LogLevels.has_value(0))
        self.assertTrue(LogLevels.has_value(10))
        self.assertTrue(LogLevels.has_value(15))
        self.assertTrue(LogLevels.has_value(20))
        self.assertTrue(LogLevels.has_value(25))
        self.assertTrue(LogLevels.has_value(30))
        self.assertTrue(LogLevels.has_value(35))
        self.assertTrue(LogLevels.has_value(40))
        self.assertTrue(LogLevels.has_value(50))

    def test_does_not_have_value(self) -> None:
        """Ensure has_value returns false for invalid values."""
        self.assertFalse(LogLevels.has_value(1))


class TestFLogger(TestCase):
    """Tests for FLogger."""

    logger: FLogger = logging.getLogger(__name__)
    msg: str = 'This is a test'

    def test_debug_logging(self) -> None:
        """Test debug logging."""
        self.logger.setLevel(LogLevels.DEBUG)

        with self.assertLogs(self.logger, LogLevels.DEBUG) as context:
            self.logger.debug(self.msg)
        self.assertEqual(context.output,
                         [f'DEBUG:{__name__}:{self.msg}'])

    def test_verbose_logging(self) -> None:
        """Test verbose logging."""
        self.logger.setLevel(LogLevels.VERBOSE)

        with self.assertLogs(self.logger, LogLevels.VERBOSE) as context:
            self.logger.verbose(self.msg)
        self.assertEqual(context.output,
                         [f'VERBOSE:{__name__}:{self.msg}'])

    def test_info_logging(self) -> None:
        """Test info logging."""
        self.logger.setLevel(LogLevels.INFO)

        with self.assertLogs(self.logger, LogLevels.INFO) as context:
            self.logger.info(self.msg)
        self.assertEqual(context.output,
                         [f'INFO:{__name__}:{self.msg}'])

    def test_notice_logging(self) -> None:
        """Test notice logging."""
        self.logger.setLevel(LogLevels.NOTICE)

        with self.assertLogs(self.logger, LogLevels.NOTICE) as context:
            self.logger.notice(self.msg)
        self.assertEqual(context.output,
                         [f'NOTICE:{__name__}:{self.msg}'])

    def test_warning_logging(self) -> None:
        """Test warning logging."""
        self.logger.setLevel(LogLevels.WARNING)

        with self.assertLogs(self.logger, LogLevels.WARNING) as context:
            self.logger.warning(self.msg)
        self.assertEqual(context.output,
                         [f'WARNING:{__name__}:{self.msg}'])

    def test_success_logging(self) -> None:
        """Test success logging."""
        self.logger.setLevel(LogLevels.SUCCESS)

        with self.assertLogs(self.logger, LogLevels.SUCCESS) as context:
            self.logger.success(self.msg)
        self.assertEqual(context.output,
                         [f'SUCCESS:{__name__}:{self.msg}'])

    def test_error_logging(self) -> None:
        """Test error logging."""
        self.logger.setLevel(LogLevels.ERROR)

        with self.assertLogs(self.logger, LogLevels.ERROR) as context:
            self.logger.error(self.msg)
        self.assertEqual(context.output,
                         [f'ERROR:{__name__}:{self.msg}'])

    def test_critical_logging(self) -> None:
        """Test critical logging."""
        self.logger.setLevel(LogLevels.CRITICAL)

        with self.assertLogs(self.logger, LogLevels.CRITICAL) as context:
            self.logger.critical(self.msg)
        self.assertEqual(context.output,
                         [f'CRITICAL:{__name__}:{self.msg}'])


class TestSetupLoggingFunction(TestCase):
    """Test the setup_logging function."""

    f_logger: logging.Logger = logging.getLogger('f-cli')
    boto3_logger: logging.Logger = logging.getLogger('boto3')
    botocore_logger: logging.Logger = logging.getLogger('botocore')

    def test_setup_logging_info(self) -> None:
        """Ensure logging levels are correct when set to INFO."""
        # set the log level high to ensure they are properly being change by setup_logging
        self.f_logger.setLevel(LogLevels.CRITICAL)
        self.boto3_logger.setLevel(LogLevels.CRITICAL)
        self.botocore_logger.setLevel(LogLevels.CRITICAL)

        setup_logging()

        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.CRITICAL))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.ERROR))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.SUCCESS))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.WARNING))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.NOTICE))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.INFO))
        self.assertFalse(self.f_logger.isEnabledFor(LogLevels.VERBOSE))
        self.assertFalse(self.f_logger.isEnabledFor(LogLevels.DEBUG))

        self.assertFalse(self.boto3_logger.isEnabledFor(LogLevels.INFO))
        self.assertFalse(self.botocore_logger.isEnabledFor(LogLevels.INFO))

    def test_setup_logging_verbose(self) -> None:
        """Ensure logging levels are correct when set to VERBOSE."""
        # set the log level high to ensure they are properly being change by setup_logging
        self.f_logger.setLevel(LogLevels.CRITICAL)
        self.boto3_logger.setLevel(LogLevels.CRITICAL)
        self.botocore_logger.setLevel(LogLevels.CRITICAL)

        setup_logging(LogLevels.VERBOSE)

        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.CRITICAL))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.ERROR))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.SUCCESS))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.WARNING))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.NOTICE))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.INFO))
        self.assertTrue(self.f_logger.isEnabledFor(LogLevels.VERBOSE))
        self.assertFalse(self.f_logger.isEnabledFor(LogLevels.DEBUG))

        self.assertFalse(self.boto3_logger.isEnabledFor(LogLevels.INFO))
        self.assertFalse(self.botocore_logger.isEnabledFor(LogLevels.INFO))

    def test_setup_logging_debug(self) -> None:
        """Ensure logging levels are correct when set to DEBUG."""
        # set the log level high to ensure they are properly being change by setup_logging
        self.f_logger.setLevel(LogLevels.CRITICAL)
        self.boto3_logger.setLevel(LogLevels.CRITICAL)
        self.botocore_logger.setLevel(LogLevels.CRITICAL)

        with self.assertLogs(self.f_logger, LogLevels.DEBUG) as setup_ctx:
            setup_logging(LogLevels.DEBUG)

            self.assertTrue(self.f_logger.isEnabledFor(LogLevels.CRITICAL))
            self.assertTrue(self.f_logger.isEnabledFor(LogLevels.ERROR))
            self.assertTrue(self.f_logger.isEnabledFor(LogLevels.SUCCESS))
            self.assertTrue(self.f_logger.isEnabledFor(LogLevels.WARNING))
            self.assertTrue(self.f_logger.isEnabledFor(LogLevels.NOTICE))
            self.assertTrue(self.f_logger.isEnabledFor(LogLevels.INFO))
            self.assertTrue(self.f_logger.isEnabledFor(LogLevels.VERBOSE))
            self.assertTrue(self.f_logger.isEnabledFor(LogLevels.DEBUG))

            self.assertTrue(self.boto3_logger.isEnabledFor(LogLevels.DEBUG))
            self.assertTrue(self.botocore_logger.isEnabledFor(LogLevels.DEBUG))

        self.assertEqual(setup_ctx.output,
                         [f'DEBUG:f-cli:Initalized logging for f-cli version {__version__}'])
