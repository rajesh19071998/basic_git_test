import requests
import pytest
from pytest_html import extras   # ✅ import extras here too

URL = "http://sw1.rajeshv.in/info"

def test_status_code(extra):
    response = requests.get(URL)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    extra.append(extras.text("✅ Status code check passed"))

def test_response_not_empty(extra):
    response = requests.get(URL)
    assert response.text.strip() != "", "Response body is empty"
    extra.append(extras.text("✅ Response body is not empty"))

def test_response_contains_board_number(extra):
    response = requests.get(URL)
    assert "5" in response.text.lower(), "Response does not contain Board number 5"
    extra.append(extras.text("✅ Response contains Board number 5"))
