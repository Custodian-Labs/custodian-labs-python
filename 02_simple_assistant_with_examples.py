from custodian_labs import Assistant


assistant = Assistant(
    model="gpt-4o",
    system_prompt="You are a helpful assistant for customer support.",
    privacy_enabled=True,
)

assistant.add_examples(
    [
        {"user": "How do I reset my password?", "assistant": "Go to settings, open security, and choose reset password."},
        {"user": "How do I invite teammates?", "assistant": "Open workspace settings, then add members by email."},
    ]
)

app = assistant.deploy()

reply = app.chat("How do I invite a new teammate?")
if reply is not None:
    print(reply.response)
    print(reply.session_id)