from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from flask import Flask, request, abort
app = Flask(__name__)

import os
from qr_code import qr_code_decode
LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET = os.environ['LINE_CHANNEL_SECRET']

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)# Channel Access Token
handler = WebhookHandler(LINE_CHANNEL_SECRET)# Channel Secret

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print("訊息從line進入:\n" + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("嚴重失敗!")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    SendImage = line_bot_api.get_message_content(event.message.id)
    local_save = './static/' + event.message.id + '.png'
    with open(local_save, 'wb') as fd:
        for chenk in SendImage.iter_content():
            fd.write(chenk)#heroku會自動清除這些圖片 吧
    info = qr_code_decode(local_save)
    print(info)
    if info != "":
        line_bot_api.reply_message(event.reply_token,TextSendMessage('已從圖片中偵測到條碼:\n' + info))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage('未從圖片中提取到任何條碼'))
    return      
        
@handler.add(MemberJoinedEvent)
def welcome(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage("歡迎將我加入群組，請直接將帶有qr code的圖片傳上來就可以讀取囉"))


@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage("歡迎將我設成朋友，請直接將帶有qr code的圖片傳上來就可以讀取囉"))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)
