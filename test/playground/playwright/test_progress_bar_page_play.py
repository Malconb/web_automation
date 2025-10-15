import pytest
import re 
from playwright.sync_api import Page, expect
from pages.playground.playwright.progress_bar_page import ProgressBarPagePlay
from dotenv import load_dotenv
import os
import time
import allure
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
    def test_progress_bar_page(self, page: Page) -> None:
        progress_bar_page = ProgressBarPagePlay(page)
        progress_bar_page.navigate()
        progress_bar_page.click_on_start()
        # Wait until progress bar reaches 75%
        while progress_bar_page.get_progress_value() != "75%":
            time.sleep(0.1)
        progress_bar_page.click_on_stop()           
        assert progress_bar_page.get_progress_value() == "75%"