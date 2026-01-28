from su25_tg_nofify import TelegramNotifier

notifier = TelegramNotifier(token, chat_id)

# Get me
notifier.get_me()

# Send message
message = """
<b>📦 New Order</b>
<pre>
Customer: John Doe
Order ID: 1024
Total: $25.00
</pre>
"""
notifier.send_message(message)

# Send photo
notifier.send_photo(
    "https://i.pinimg.com/1200x/80/27/c6/8027c6c615900bf009b322294b61fcb2.jpg",
    caption="this is chhing chang",
)

# Send document
notifier.send_document(
    "https://pdfobject.com/pdf/sample.pdf",
    caption="this is an example about this project",
)