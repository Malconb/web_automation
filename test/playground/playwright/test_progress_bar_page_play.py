import pytest
import re 
from playwright.sync_api import Page, expect
from pages.playground.playwright.progress_bar_page import ProgressBarPagePlay
from dotenv import load_dotenv
import os
import time
import allure
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
    def test_progress_bar_page(self, page: Page, log_test_name) -> None:
        progress_bar_page = ProgressBarPagePlay(page)
        progress_bar_page.navigate()
        progress_bar_page.click_on_start()
        # Wait until progress bar reaches 75%
        while progress_bar_page.get_progress_value() < "75%":
            None
        progress_bar_page.click_on_stop()           
        assert progress_bar_page.get_progress_value() >= "75%"
        logger.info("Progress bar reached " + progress_bar_page.get_progress_value() + " for stopping")