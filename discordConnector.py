import requests
def send_message(message):
    url = "https://1e24e999cd8c.ngrok.io/webhooks/rest/webhook"
    data = {
        "sender":"discord",
        "message":""+message
    }
    reply = requests.post(url,json=data)
    return reply.json()[0]['text']

def parse_bot_message(json_message):
    
send_message('Hello')