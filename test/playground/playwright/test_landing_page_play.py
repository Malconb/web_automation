"""
test for Landing page play
"""
import pytest
import allure
from playwright.sync_api import Page, expect
from pages.playground.playwright.landing_page_play import LandingPagePlay
from utils.logger import get_logger
from utils.soft_assert import SoftAssert

logger = get_logger(__name__)
soft_assert = SoftAssert()

@allure.title("Test Smoke for Landing page")
@allure.description("This test verifies landing page for Test Automation Playground.")
@allure.tag("Landing", "Smoke", "Functional")
@pytest.mark.functional
@pytest.mark.landing_page
class TestLandingPagePlay:
    """
    test class for landing page play
    """
    @pytest.mark.xfail(reason="Alerts section still in progress", strict=True)
    @pytest.mark.landing_page
    def test_landing_page(self, page: Page, log_test_name) -> None:
        """
        test for landing page play
        """
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        expect(page).to_have_title("UI Test Automation Playground")
        assert landing_page.sample_app.is_visible()
        logger.info("Sample App is visible")
        assert landing_page.dynamic_id.is_visible()
        logger.info("Dynamic ID is visible")
        assert landing_page.progress_bar.is_visible()
        logger.info("Progress Bar is visible")
        
        #Soft assert
        soft_assert.verify(
            landing_page.alerts.is_visible(),
            "Alert de landing page no está visible"
        )
        logger.info("Alerts verification attempted (soft assert)")
        soft_assert.assert_all()
