from .client import TelegramClient

class TelegramNotifier:
    def __init__(self, token: str, chat_id: str):
        self.chat_id = chat_id
        self.client = TelegramClient(token)

    def get_me(self):
        return self.client.post("getMe", payload=None)

    def send_message(
        self,
        text: str,
        parse_mode: str = "HTML",
        disable_notification: bool = False,
        disable_web_page_preview: bool = False,
    ):
        payload = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_notification": disable_notification,
            "disable_web_page_preview": disable_web_page_preview,
        }
        return self.client.post("sendMessage", payload)

    def send_photo(
        self,
        photo_url: str,
        caption: str | None = None,
        disable_notification: bool = False,
    ):
        payload = {
            "chat_id": self.chat_id,
            "photo": photo_url,
            "caption": caption,
            "disable_notification": disable_notification,
        }
        return self.client.post("sendPhoto", payload)

    def send_document(
        self,
        document_url: str,
        caption: str | None = None,
        disable_notification: bool = False,
    ):
        payload = {
            "chat_id": self.chat_id,
            "document": document_url,
            "caption": caption,
            "disable_notification": disable_notification,
        }
        return self.client.post("sendDocument", payload)
