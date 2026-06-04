from custodian_labs import create_assistant


app = create_assistant(
    model="gpt-4o",
    prompt="You are a helpful assistant for onboarding new users.",
    privacy_enabled=True,
)

print(app.chat_url)

reply = app.chat("What should a new admin do first?")
if reply is not None:
    print(reply.response)