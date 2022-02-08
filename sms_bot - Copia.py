# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe70c373c58f6436d1c1486d6e41ab9c2'
auth_token = '3acace0c78f26a413bdf58b545b7be91'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=""" Teste de envio SMS via Python """,
         from_='+5534933007290',
         status_callback='http://postb.in/1234abcd',
         #to='+5548985052905'
         to='+5548985057720'
     )

print(message.sid)


### we import the Twilio client from the dependency we just installed
##from twilio.rest import Client
##
### the following line needs your Twilio Account SID and Auth Token
##client = Client("ACe70c373c58f6436d1c1486d6e41ab9c2", "3acace0c78f26a413bdf58b545b7be91")
##
### change the "from_" number to your Twilio number and the "to" number
### to the phone number you signed up for Twilio with, or upgrade your
### account to send SMS to any phone number
##client.messages.create(to="+5548985052905", 
##                       from_="+5548985052905", 
##                       body="Hello from Python!")
