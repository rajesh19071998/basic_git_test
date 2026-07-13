import requests

def test_http_get_example():
    url = "http://sw1.rajeshv.in/info"
    response = requests.get(url)

    # Check 1: Status code must be 200
    assert response.status_code == 200, f"❌ Expected 200, got {response.status_code}"

    # Check 2: Response must not be empty
    assert response.text.strip() != "", "❌ Response body is empty"

    # Check 3: Response must contain keyword 'info'
    assert "5" in response.text.lower(), "❌ Response does not contain Board number 5'"

if __name__ == "__main__":
    test_http_get_example()