import json
from Debt_Simplification import *
from copy import deepcopy

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
payment = minCashFlowRec(amount, [])
print(payment)

for i in payment:
    copyFlexMSG = deepcopy(flexMSG)
    copyFlexMSG["contents"][0]["text"] = str(i[0]) + " needs to pay " + str(i[2])
    copyFlexMSG["contents"][1]["text"] = str(i[1]) + "元"
    basicFormat["body"]["contents"].append(copyFlexMSG)

print("\n\n\n")
print( json.dumps(basicFormat,indent=4) )
