import pytest
import re 
from playwright.sync_api import Page
from pages.playground.playwright.alerts_page_play import AlertsPagePlay
from dotenv import load_dotenv
import os
import allure
from utils.logger import get_logger

logger = get_logger(__name__)

username = os.getenv("username")
password = os.getenv("password")
password2 = os.getenv("password2")


@allure.title("Test Smoke for Sample App page")
@allure.description("This test verifies Sample App page for Test Automation Playground.")
@allure.tag("Sample App", "Smoke", "Functional")
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.alerts_page
class TestAlertsPlay:
 
    @pytest.mark.alerts_page_success
    def test_alerts_success(self, page: Page, log_test_name) -> None:
        alerts_page = AlertsPagePlay(page)
        alerts_page.navigate()
        alerts_page.click_on_alert_button()
        logger.info("Alert button was clicked")
        alerts_page.click_on_confirm_button()
        logger.info("Confirm button was clicked")
        alerts_page.click_on_prompt_button()
        logger.info("Prompt button was clicked")
               
    @pytest.mark.alerts_page_parametrize("read_data", ["link"], indirect=True)
    def test_alerts_successparametrized(self, page: Page, read_data, log_test_name) -> None:
        alerts_page = AlertsPagePlay(page)
        alerts_page.navigate()
        for data in read_data:
            alerts_page.click_on_parametrized_button(data["button"])
            logger.info(data["clicked_button"])