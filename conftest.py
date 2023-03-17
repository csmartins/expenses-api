import os
import pytest

try:
    from.temp_env_var import TEMP_ENV_VARS, ENV_VARS_TO_SUSPEND
except ImportError:
    TEMP_ENV_VARS = {}
    ENV_VARS_TO_SUSPEND = []

TEMP_MONGO_ENV_VARS = {
    "MONGODB_CONNSTRING": "",
    "MONGODB_DATABASE": ""
}


@pytest.fixture(scope="session", autouse=True)
def tests_setup_and_teardown():
    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEMP_MONGO_ENV_VARS)

    yield
    # Will be executed after the last test
    os.environ.clear()
    os.environ.update(old_environ)