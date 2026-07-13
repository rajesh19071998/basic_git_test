import requests

url = "http://sw1.rajeshv.in/info"
# Example: HTTP GET request (text response)
def http_get_example():
    #url = "https://httpbin.org/get"
    response = requests.get(url)
    
    # Assert that the request succeeds
    assert response.status_code == 200
    # Optionally check response contains expected text
    assert "info" in response.text.lower()

    if response.status_code == 200:
        print("GET Response (text):")
        print(response.text)   # raw text output
    else:
        print(f"GET request failed with status code {response.status_code}")


if __name__ == "__main__":
    http_get_example()






url = "http://sw1.rajeshv.in/info"

def test_http_get_example():
    response = requests.get(url)
    # Assert that the request succeeds
    assert response.status_code == 200
    # Optionally check response contains expected text
    assert "info" in response.text.lower()


