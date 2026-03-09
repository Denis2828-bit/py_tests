from playwright.sync_api import Page


class MainPage:
    """Page Object for https://reqres.in main page."""

    URL = "/"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self):
        self.page.goto(self.base_url + self.URL)

    def get_title(self) -> str:
        return self.page.title()

    def click_get_started(self):
        self.page.locator("text=Get Started").first.click()

    def get_console_output(self) -> str:
        return self.page.locator("#console").inner_text()
