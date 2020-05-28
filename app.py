from flask import Flask, request, abort
#用flask架設伺服器，屬於網頁程式碼

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('RtQqMycABt/dX6OHyOT0y1Ys8KAsOnec/BDHZYoEND/Gu/AkUnf1DfMdG/z3nYi+fDTY2y6DHXlu9yYi7ryj1Wrq4V7wpXZIH45QUFIgMArEki4e0nHoSdZl0BHGA/zCQQr46pqhC+/JRMSvEIoO4AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d8dc46f7cf040b8437e9cf8c46c332a8')


@app.route("/callback", methods=['POST'])
#如果有人輸入的網址是例如www.bingbond.com/callback，才會執行下面程式碼
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#處理接收到的訊息fuction
    line_bot_api.reply_message(
        #回覆訊息的功能
        event.reply_token,
        TextSendMessage(text=event.message.text))



if __name__ == "__main__":
#line-bot.py可以被import載入，如果不寫上面這一行，那載入就會直接執行，這一行的意思就是我叫他執行再執行
    app.run()





