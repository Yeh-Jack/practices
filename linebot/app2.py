from flask import Flask, request, abort

# pip install line-bot-sdk==1.8.0

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

# Channel Access Token
LINE_TOKEN = os.environ.get("LINE_TOKEN")
line_bot_api = LineBotApi(LINE_TOKEN)
# Channel Secret
LINE_HOOK_SECRET = os.environ.get("LINE_HOOK_SECRET")
handler = WebhookHandler(LINE_HOOK_SECRET)


def buildLocation(latitude, longitude, title="Unknow", address="Unknown"):
    return LocationSendMessage(
        title=title, address=address, latitude=latitude, longitude=longitude
    )


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
        buildLocation(25.032977597205768, 121.52808257163666),
        buildLocation(
            25.034571833791116,
            121.53233119127395,
            title="鼎泰豐 新生店",
            address="臺北市中正區三愛里信義路二段277號",
        ),
    ]
    line_bot_api.reply_message(event.reply_token, messages)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
