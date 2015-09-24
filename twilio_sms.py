from twilio.rest import TwilioRestClient

ACCOUNT_SID='AC53e32563fcc5c585a494d1e0ac64f5c2'
AUTH_TOKEN='f913521984cf8eb7af859cc53769808a'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(body="Help! I'm trapped in a text factory!",
                                 to="+12402742942",
                                 from_="+12408835876")
print message.sid
