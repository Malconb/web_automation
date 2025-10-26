from playwright.sync_api import Page, Locator
from pages.playground.playwright.base_page_play import BasePagePlay
from utils.logger import get_logger

logger = get_logger(__name__)

class ProgressBarPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        #locator
        self.start : Locator = page.get_by_role("button", name="Start")
        self.stop : Locator = page.get_by_role("button", name="Stop")
        self.progress_bar : Locator = page.locator("#progressBar")

    def navigate(self):
        self.navigate_url("http://uitestingplayground.com/ProgressBar")
        
    def click_on_start(self):
        self.click_on_element(self.start)
        logger.info("Clicked on Start button")  
        
    def click_on_stop(self):
        self.click_on_element(self.stop)
        logger.info("Clicked on Stop button") 
        
    def get_progress_value(self) -> str:
        logger.info("Getting progress value: " + self.progress_bar.text_content().strip())
        return self.progress_bar.text_content().strip()
        