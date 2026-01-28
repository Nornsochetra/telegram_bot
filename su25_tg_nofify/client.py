import requests

class TelegramClient:
    def __init__(self, token: str, user_agent: str = "so chetraa"):
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.headers = {
            "accept": "application/json",
            "User-Agent": user_agent,
            "content-type": "application/json",
        }

    def post(self, endpoint: str, payload: dict):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=payload, headers=self.headers)
        print(response.text)
        response.raise_for_status()
        return response.json()
