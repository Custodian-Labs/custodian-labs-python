from custodian_labs import create_assistant


app = create_assistant(
    model="gpt-4o",
    prompt="You are a helpful assistant for onboarding new users.",
    privacy_enabled=True,
)

print(app.chat_url)

# Chat using default model (gpt-4o)
reply = app.chat("What should a new admin do first?")
if reply is not None:
    print(reply.response)

# Optional: Override model for this chat request
# reply = app.chat("What should a new admin do first?", model="claude-3.5-sonnet")
# if reply is not None:
#     print(reply.response)