from flask import Flask, request, abort

# pip install line-bot-sdk==1.8.0

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    "RKbQi93iMFkjG4gzEufbKfc1eHWVDNpfdnAlwolcYwPOAeYVjpTycgzxAV3XfQmrigCZaSTGE2RnFKDv9tzV1/eaBy1ODl4yZotcFQpH8pwhqhuGVSMJNMzZnJlmBVS2n0Ib2alhTaaSY4kXQnpGtwdB04t89/1O/w1cDnyilFU="
)
# Channel Secret
handler = WebhookHandler("52e5c8d6bc6f110a13486f3db80acf6b")


def buildSticker(packageId, stickerId):
    return StickerMessage(package_id=packageId, sticker_id=stickerId)


def buildText(message):
    return TextSendMessage(text=message)


# 監聽所有來自 /hook 的 Post Request
@app.route("/hook", methods=["POST"])
def hook():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    client_message = event.message.text
    print(client_message)

    messages = [
        buildText(f"> {client_message} !!"),
        buildSticker("11537", "52002734"),
        buildSticker("2", "46"),
        buildSticker("4", "618"),
    ]
    line_bot_api.reply_message(event.reply_token, messages)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
