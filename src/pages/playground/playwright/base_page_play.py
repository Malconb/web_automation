from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePagePlay(Page):
    def __init__(self, page: Page):
        self.page = page

    def navigate_url(self, url):
        logger.info(f"Navigating to the page: {url}")
        self.page.goto(url)

    def click_on_element(self, locator):
        tag_name = locator.evaluate("node => node.tagName")
        logger.info(f"Clicking on {locator.text_content()} element: {tag_name}")
        locator.click()

    def fill_element(self, locator, text):
        tag_name = locator.evaluate("node => node.tagName")
        logger.info(f"Filling '{text}' in element: {tag_name}")
        locator.fill(text)
        
        