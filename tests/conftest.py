"""Configure pytest."""
from typing import Dict
import logging
import os

import pytest

LOG = logging.getLogger(__name__)


@pytest.fixture(scope='session', autouse=True)  # type: ignore
def aws_credentials() -> None:
    """Ensure AWS SDK finds some (bogus) credentials in the environment.

    Handles change in https://github.com/spulec/moto/issues/1924

    """
    overrides: Dict[str, str] = {
        'AWS_ACCESS_KEY_ID': 'testing',
        'AWS_SECRET_ACCESS_KEY': 'testing',
        'AWS_DEFAULT_REGION': 'us-east-1'
    }
    saved_env: Dict[str, str] = {}
    for key, value in overrides.items():
        LOG.info('Overriding env var: %s=%s', key, value)
        saved_env[key] = os.environ.get(key, '')
        os.environ[key] = value

    yield

    for key, value in saved_env.items():
        LOG.info('Restoring saved env var: %s=%s', key, value)
        if value is None:
            del os.environ[key]
        else:
            os.environ[key] = value

    saved_env.clear()
