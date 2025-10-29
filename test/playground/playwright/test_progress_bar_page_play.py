"""
test for Progress Bar page play
"""

import os
import time
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from pages.playground.playwright.progress_bar_page import ProgressBarPagePlay
from utils.logger import get_logger

logger = get_logger(__name__)

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
password2 = os.getenv("password2")

@allure.title("Test Smoke for Progress Bar page")
@allure.description("This test verifies Progress Bar page for Test Automation Playground.")
@allure.tag("Progress Bar", "Smoke", "Functional")
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.progress_bar_page
class TestProgressBarPagePlay:
    """
    test class for progress bar page play
    """

    @pytest.mark.progress_bar_page
    def test_progress_bar_page(self, page: Page, log_test_name) -> None:
        """
        test for progress bar page play
        """
        progress_bar_page = ProgressBarPagePlay(page)
        progress_bar_page.navigate()
        progress_bar_page.click_on_start()
        # Wait until progress bar reaches 75%
        while progress_bar_page.get_progress_value() < "75%":
            time.sleep(0.5)
        progress_bar_page.click_on_stop()
        assert progress_bar_page.get_progress_value() >= "75%"
        logger.info("Progress bar reached " + progress_bar_page.get_progress_value() + " for stop")
        