import re 
from playwright.sync_api import Page, expect
from pages.playground.playwright.sample_app_page_play import SampleAppPagePlay

class TestSampleAppPlay:

    def test_sample_app_login_success(self, page: Page) -> None:
        sample_app_page = SampleAppPagePlay(page)
        sample_app_page.navigate()
        sample_app_page.click_on_textbox()
        sample_app_page.enter_text("Miguel")
        sample_app_page.click_on_password()
        sample_app_page.enter_password("pwd")
        sample_app_page.click_on_login()
        assert page.get_by_text("Welcome, Miguel!").is_visible()
        sample_app_page.click_on_logout()
        assert page.get_by_text("User logged out.").is_visible()

    def test_sample_app_login_failure(self, page: Page) -> None:
        sample_app_page = SampleAppPagePlay(page)
        sample_app_page.navigate()
        sample_app_page.click_on_textbox()
        sample_app_page.enter_text("Miguel")
        sample_app_page.click_on_password()
        sample_app_page.enter_password("wrong pwd")
        sample_app_page.click_on_login()
        assert page.get_by_text("Invalid username/password").is_visible()
        
        #page.goto("http://uitestingplayground.com/")
        #page.get_by_role("link", name="Sample App").click()
        #page.get_by_role("textbox", name="User Name").click()
        #page.get_by_role("textbox", name="User Name").fill("Miguel")
        #page.get_by_role("textbox", name="User Name").press("Tab")
        #page.get_by_role("textbox", name="********").fill("pwd")
        #page.get_by_role("button", name="Log In").click()
        #page.get_by_text("Welcome, Miguel!").click()
        #page.get_by_text("Welcome, Miguel!").click()
        #page.get_by_role("button", name="Log Out").click()
        #page.get_by_text("User logged out.").click()
        #page.get_by_role("textbox", name="User Name").click()
        #page.get_by_role("textbox", name="User Name").fill("Miguel")
        #page.get_by_role("textbox", name="********").click()
        #page.get_by_role("textbox", name="********").fill("otherpswd")
        #page.get_by_role("button", name="Log In").click()
        #page.get_by_text("Invalid username/password").click()
