from twilio.rest import Client

client = Client(
    "ACebab0ba2072e1c5ec1bd27c52eb8c601",
    "7278ac67ad93881222154f24e6167d00"
)

# for msg in client.messages.list():
#     print(msg.body)

# To delete entire messages from Twilio account.
# for msg in client.messages.list():
#     print(f"Deleting {msg.body}")
#     msg.delete()

msg = client.messages.create(
    to="+918374628422",
    from_="+12073863492",
    body="Hello from Python"
)

print(f"Created a new message: {msg.sid}")
