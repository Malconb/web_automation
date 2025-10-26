from playwright.sync_api import Page, Locator
from pages.playground.playwright.base_page_play import BasePagePlay
from utils.logger import get_logger

logger = get_logger(__name__)

class AlertsPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        
        #locator
        self.alert_button : Locator = page.get_by_role("button", name="Alert")
        self.confirm_button : Locator = page.get_by_role("button", name="Confirm")
        self.prompt_button : Locator = page.get_by_role("button", name="Prompt")
        self.blocked_button : Locator = page.get_by_role("button", name="Blocked")

        self.locator_link = {
            "Alert": self.alert_button,
            "Confirm": self.confirm_button,
            "Prompt": self.prompt_button,
            "Blocked": self.blocked_button,
        }

    def navigate(self):
        self.navigate_url("http://uitestingplayground.com/Alerts")

    def click_on_alert_button(self):
        self.click_on_element(self.alert_button)

    def click_on_confirm_button(self):
        self.click_on_element(self.confirm_button)

    def click_on_prompt_button(self):
        self.click_on_element(self.prompt_button)

    def click_on_parametrized_button(self, data):
        self.click_on_element(self.locator_link[data])