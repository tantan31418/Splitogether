from django.conf import settings
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *

from Debt_Simplification import *
from line.models import *
import json
from copy import deepcopy



line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)



#Reply Payment list request with a Flex message
def replyPaymentFlex(event):

    with open('PaymentFlexMSG.json') as f:
        basicFormat = json.load(f)

    flexMSG = {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "arrrrrr",
            "align": "center",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "",
            "gravity": "center",
            "align": "end"
          }
        ],
        "borderWidth": "5px"
      }

    amount = {
	"userID1": 5000,
	"userID2": 3000,
	"userID3": -4000,
	"userID4": -4000
    }
    #TanTan DB TODO

    payment = minCashFlowRec(amount, [])

    for i in payment:
        copyFlexMSG = deepcopy(flexMSG)
        copyFlexMSG["contents"][0]["text"] = str(i[0]) + " needs to pay " + str(i[2])
        copyFlexMSG["contents"][1]["text"] = str(i[1]) + "元"
        basicFormat["contents"]["body"]["contents"].append(copyFlexMSG)
    
    print( json.dumps(basicFormat,indent=4) )
    return basicFormat