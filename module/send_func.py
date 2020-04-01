from django.conf import settings
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *

from module.Debt_Simplification import *
from line.models import 

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)



#Reply Payment list request with a Flex message
def replyPaymentFlex(event):
    amount = {
	"userID1": 5000,
	"userID2": 3000,
	"userID3": -4000,
	"userID4": -4000
    }
    payment = minCashFlowRec(amount, [])

    TextArray = ""
    for i in payment:
        TextArray = ' '.join( [TextArray, "Person", str(i[0]), "pays ", str(i[1]),"to" ,"Person" ,str(i[2]), '\n' ] )

    flexMSG = {
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "阮棠欠佐任",
                            "align": "center",
                            "gravity": "center"
                        },
                        {
                            "type": "text",
                            "text": " 1000元",
                            "gravity": "center"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "clear1",
                            "data": "clearPayment#1"
                            },
                            "style": "primary"
                        }
                        ],
                        "borderWidth": "5px"
                    }
                    ]
                }  
            }

