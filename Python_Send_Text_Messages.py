from twilio.rest import Client

account_sid = "" # enter account_sid from Twilio API
auth_token = "" # enter auth_token from Twilio API
client = Client(account_sid, auth_token)

call = Client.messages.create(
    to="", # enter the recipient phone number
    from="", # enter the phone number associated with Twilio account
    body="" # message body
)

print("Succesfully sent") 
