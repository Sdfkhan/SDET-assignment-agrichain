import pytest
from pages.home_page import HomePage
from pages.result_page import ResultPage

def test_longest_substring_valid_input(page):
    home = HomePage(page)
    result = ResultPage(page)

    page.goto("https://agrichain.com/qa/input")

    home.enter_text("abcabcbb")
    home.submit()

    output = result.get_output()
    assert output == "3"
