import pytest
import logging
from utils.logger import get_logger

from utils.logger import get_logger

logger = get_logger(__name__)

class TestExample():

    # fixture
    def setup_class(self):
        logger.debug("Setup class")
        self.environment = pytest.env
        logger.debug("Environment: %s", self.environment)
        self.browser = pytest.browser
        logger.debug("Browser: %s", self.browser)

    def setup_method(self):
        logger.debug("Setup method")

    def test_one(self):
        logger.debug("test one ")

    def test_two(self, first_entry):
        logger.debug("test two : %s", first_entry)

    def test_three(self, order):
        logger.debug("test three: %s", order)

    # fixture
    def teardown_method(self):
        logger.debug("tearDown")

    def teardown_class(self):
        logger.debug("tearDown Class")