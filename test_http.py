import requests
import pytest
from pytest_html import extras   # ✅ import extras here too

URL = "http://sw1.rajeshv.in/info"

def test_board_info(extra):
    # Run PlatformIO CLI command
    result = subprocess.run(
        ["pio", "boards", "esp32doit-devkit-v1"],
        capture_output=True,
        text=True
    )

    # Ensure command succeeded
    assert result.returncode == 0, "❌ pio boards command failed"

    # ✅ Attach CLI output to HTML report (collapsible)
    extra.append(extras.html(
        "<details><summary>ESP32 DevKit v1 Board Info</summary>"
        f"<pre>{result.stdout}</pre></details>"
    ))

def test_status_code(extra):
    response = requests.get(URL)
    assert response.status_code == 200, f"❌ Expected 200, got {response.status_code}"
    extra.append(extras.text("✅ Status code check passed"))

def test_response_not_empty(extra):
    response = requests.get(URL)
    assert response.text.strip() != "", "❌ Response body is empty"
    extra.append(extras.text("✅ Response body is not empty"))

def test_response_board_num_match(extra):
    response = requests.get(URL)
    assert "Board_Number : 5" in response.text, "❌ Response board number not 5"
    extra.append(extras.text("✅ Response body board number was 5"))

    assert "Board_Name : SWITCH_BOARD_1" in response.text, "❌ Response Board_Name : SWITCH_BOARD_1 not found"
    extra.append(extras.text("✅ Response body board name was SWITCH_BOARD_1"))

    assert "Board Local DNS : http://switch_board_1.local" in response.text, "❌ Response Board Local DNS not found"
    extra.append(extras.text("✅ Response body board local DNS was http://switch_board_1.local"))



