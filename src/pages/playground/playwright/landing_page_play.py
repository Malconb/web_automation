from playwright.sync_api import Page, Locator
from pages.playground.playwright.base_page_play import BasePagePlay
from pages.playground.playwright.sample_app_page_play import SampleAppPagePlay
from pages.playground.playwright.progress_bar_page import ProgressBarPagePlay


class LandingPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        #locator
        self.textbox : Locator = page.get_by_role("textbox", name="User Name")
        self.sample_app : Locator = page.get_by_role("link", name="Sample App")
        self.dynamic_id : Locator = page.get_by_role("link", name="Dynamic ID")
        self.progress_bar : Locator = page.get_by_role("link", name="Progress Bar")
        
    def navigate(self):
        self.navigate_url("http://uitestingplayground.com/")
    
    def click_on_sample_app(self):
        self.click_on_element(self.sample_app)
        return SampleAppPagePlay(self.page)
    
    def click_on_progress_bar(self):
        self.click_on_element(self.progress_bar)
        return ProgressBarPagePlay(self.page)