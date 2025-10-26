from playwright.sync_api import Page

def test_page_type(page: Page):
    print(type(page))
    assert "Page" in str(type(page)) 