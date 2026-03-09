import pytest
from pages.main_page import MainPage


@pytest.mark.ui
@pytest.mark.smoke
class TestMainPage:
    def test_page_title_is_correct(self, page, base_ui_url):
        main = MainPage(page, base_ui_url)
        main.open()
        assert "DummyJSON" in main.get_title()

    def test_page_loads_successfully(self, page, base_ui_url):
        main = MainPage(page, base_ui_url)
        main.open()
        assert page.url.startswith(base_ui_url)
