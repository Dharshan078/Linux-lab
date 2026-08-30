import requests

try:
    response = requests.get('https://api.github.com/', timeout = 5)
    response.raise_for_status()
    print("API request succeed")
    print("Status Code      :",response.status_code)
    print("Header           :",response.headers)
    data = response.json()
    print("JSON             :",data)
    print("\ncurrent_user_url:",data["current_user_url"])

except requests.exceptions.ConnectionError as e:
    print(f"API Connection failed: {e}")

except requests.exceptions.Timeout as e:
    print(f"API Timed Out: {e}")

except requests.exceptions.HTTPError as e:
    print(f"API request failed: {e}")

