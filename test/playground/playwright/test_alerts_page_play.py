"""
test for Alerts page play
"""

import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from pages.playground.playwright.alerts_page_play import AlertsPagePlay
from utils.logger import get_logger

logger = get_logger(__name__)

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
password2 = os.getenv("password2")


@allure.title("Test Smoke for Alerts page")
@allure.description("This test verifies Alerts page for Test Automation Playground.")
@allure.tag("Alerts", "Smoke", "Functional")
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.alerts_page
class TestAlertsPlay:
    """
    test class for Alerts page play
    """

    @pytest.mark.alerts_page_success
    def test_alerts_success(self, page: Page, log_test_name) -> None:
        """
        test for Alerts page play
        """
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
        """
        test for Alerts page play parametrized
        """
        alerts_page = AlertsPagePlay(page)
        alerts_page.navigate()
        for data in read_data:
            alerts_page.click_on_parametrized_button(data["button"])
            logger.info(data["clicked_button"])
