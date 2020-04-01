from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *
from module.Debt_Simplification import *



line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            if isinstance(event, MessageEvent):
                amount = {"userID1": 5000, "userID2": 3000,	"userID3": -4000, "userID4": -4000}
                payment = minCashFlowRec(amount, [])
                TextArray = ""
                for i in payment:
                    TextArray = ' '.join( [TextArray, "Person", str(i[0]), "pays ", str(i[1]),"to" ,"Person" ,str(i[2]), '\n' ] )
                line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                        text=TextArray), TextSendMessage(text='echo')])
                '''
                line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                        text=event.message.text), TextSendMessage(text='echo')])
                '''


        return HttpResponse()
    else:
        return HttpResponseBadRequest()
