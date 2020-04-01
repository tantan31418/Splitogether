import json

flexMSG = {
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








with open('PaymentFlexMSG.json') as f:
    type_size_header = json.load(f)

type_size_header["body"]["contents"].append(dict(flexMSG))



print( json.dumps(type_size_header,indent=4,sort_keys=True) )
