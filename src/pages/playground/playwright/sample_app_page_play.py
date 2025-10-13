from playwright.sync_api import Page, Locator
from pages.playground.playwright.base_page_play import BasePagePlay

class SampleAppPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        #locator
        self.textbox : Locator = page.get_by_role("textbox", name="User Name")
        self.password : Locator = page.get_by_role("textbox", name="********")
        self.login : Locator = page.get_by_role("button", name="Log In")
        self.logout : Locator = page.get_by_role("button", name="Log Out")
    
    def navigate(self):
        self.navigate_url("http://uitestingplayground.com/")
        self.page.get_by_role("link", name="Sample App").click()

    def click_on_textbox(self):
        self.click_on_element(self.textbox)

    def click_on_password(self):
        self.click_on_element(self.password)

    def enter_text(self, text):
        self.fill_element(self.textbox, text)

    def enter_password(self, password):
        self.fill_element(self.password, password)

    def click_on_login(self):
        self.click_on_element(self.login)

    def click_on_logout(self):
        self.click_on_element(self.logout)

    