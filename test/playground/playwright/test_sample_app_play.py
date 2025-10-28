import pytest
import re 
from playwright.sync_api import Page, expect
from pages.playground.playwright.sample_app_page_play import SampleAppPagePlay
from dotenv import load_dotenv
import os
import allure
from utils.logger import get_logger

logger = get_logger(__name__)
load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
password2 = os.getenv("password2")


@allure.title("Test Smoke for Sample App page")
@allure.description("This test verifies Sample App page for Test Automation Playground.")
@allure.tag("Sample App", "Smoke", "Functional")
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.sample_app_page
class TestSampleAppPlay:

    @pytest.mark.login_success
    def test_sample_app_login_success(self, page: Page, log_test_name) -> None:
        sample_app_page = SampleAppPagePlay(page)
        sample_app_page.navigate()
        sample_app_page.enter_text(username)
        sample_app_page.enter_password(password)
        sample_app_page.click_on_login()
        assert page.get_by_text("Welcome, Miguel!").is_visible()
        logger.info("User logged in successfully")
        sample_app_page.click_on_logout()
        assert page.get_by_text("User logged out.").is_visible()
        logger.info("User logged out successfully")


    @pytest.mark.login_failure
    def test_sample_app_login_failure(self, page: Page, log_test_name) -> None:
        sample_app_page = SampleAppPagePlay(page)
        sample_app_page.navigate()
        sample_app_page.enter_text(username)
        sample_app_page.enter_password(password2)
        sample_app_page.click_on_login()
        assert page.get_by_text("Invalid username/password").is_visible()
        logger.info("Login failed successfully")


