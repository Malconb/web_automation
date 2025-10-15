from playwright.sync_api import Page, Locator
from pages.playground.playwright.base_page_play import BasePagePlay

class ProgressBarPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        #locator
        self.start : Locator = page.get_by_role("button", name="Start")
        self.stop : Locator = page.get_by_role("button", name="Stop")
        self.progress_bar : Locator = page.locator("#progressBar")

    def navigate(self):
        self.navigate_url("http://uitestingplayground.com/")
        self.page.get_by_role("link", name="Progress Bar").click()
        
    def click_on_start(self):
        self.click_on_element(self.start)
        
    def click_on_stop(self):
        self.click_on_element(self.stop)
        
    def get_progress_value(self) -> str:
        return self.progress_bar.text_content().strip()
        