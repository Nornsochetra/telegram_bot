import requests
from time import sleep

# testing token is it work or not
# url = f"https://api.telegram.org/bot{token}/getMe"
#
# headers = {
#     "accept": "application/json",
#     "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)"
# }
#
# response = requests.post(url, headers=headers)
#
# print(response.text)

# send notification
url = f"https://api.telegram.org/bot{token}/sendMessage"

payload = {
    "text": "hello world my name is chetra", # text we want to see
    "parse_mode": "HTML", # format text
    "disable_web_page_preview": False,
    "disable_notification": False,
    "chat_id": "@su25_notification_testing" # username group
}
headers = {
    "accept": "application/json",
    "User-Agent": "so chetraa",
    "content-type": "application/json"
}

for response in range(100):
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    sleep(3)