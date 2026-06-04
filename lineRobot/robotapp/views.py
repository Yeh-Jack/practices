from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    LocationSendMessage,
    ImageSendMessage,
)

from dotenv import load_dotenv
import os, re

load_dotenv()


# Channel Access Token
# LINE_TOKEN = os.environ.get("LINE_TOKEN")
LINE_TOKEN = os.getenv("LINE_TOKEN")
line_bot_api = LineBotApi(LINE_TOKEN)
# WebHook Secret
# LINE_HOOK_SECRET = os.environ.get("LINE_HOOK_SECRET")
LINE_HOOK_SECRET = os.getenv("LINE_HOOK_SECRET")
handler = WebhookHandler(LINE_HOOK_SECRET)


@csrf_exempt
def callback(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        # get X-Line-Signature header value
        signature = request.META["HTTP_X_LINE_SIGNATURE"]

        # get request body as text
        body = request.body.decode("utf-8")

        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseBadRequest()

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@handler.add(MessageEvent, message=TextMessage)
def message_text(event: MessageEvent):
    a = event.message.text
    if re.search(r"(?:Japan|日本)", a, re.IGNORECASE):
        message = LocationSendMessage(
            title="Tokyo", address="東京", latitude=35.659108, longitude=139.7037
        )
    # line_bot_api.reply_message(event.reply_token, message)
    elif re.search(r"(?:Taiwan|[台臺]灣)", a, re.IGNORECASE):
        message = LocationSendMessage(
            title="Taipei", address="台北", latitude=25.035054, longitude=121.521208
        )
    # line_bot_api.reply_message(event.reply_token, message)
    elif re.search(r"(?:Korea|韓國)", a, re.IGNORECASE):
        message = LocationSendMessage(
            title="Sou", address="首爾", latitude=37.551653, longitude=126.986922
        )
    # line_bot_api.reply_message(event.reply_token, message)
    elif re.search(r"\bstudy\b", a, re.IGNORECASE):
        message = TextSendMessage("Use the [speak] project.")
    else:
        message = TextSendMessage("請輸入相關文字,暫時不支援其他功能")
    line_bot_api.reply_message(event.reply_token, message)


# line_bot_api.reply_message(
#     event.reply_token,
#     TextSendMessage(text=event.message.text)
# )
