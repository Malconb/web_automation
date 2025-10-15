import pytest
import re  
import allure
from playwright.sync_api import Page, expect
from pages.playground.playwright.landing_page_play import LandingPagePlay

@allure.title("Test Smoke for Landing page")
@allure.description("This test verifies landing page for Test Automation Playground.")
@allure.tag("Landing", "Smoke", "Functional")
@pytest.mark.functional
@pytest.mark.smoke 
class TestLandingPagePlay:
    """
    test class for landing page play
    """

    def test_landing_page(self, page: Page) -> None:
        landing_page = LandingPagePlay(page)
        landing_page.navigate()

        expect(page).to_have_title("UI Test Automation Playground")
        expect(landing_page.sample_app).to_be_visible()
        expect(landing_page.sample_app).to_contain_text("Sample App")
        expect(landing_page.dynamic_id).to_contain_text("Dynamic ID")
        expect(landing_page.progress_bar).to_contain_text("Progress Bar")
