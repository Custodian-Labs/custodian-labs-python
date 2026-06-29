from custodian_labs import Custodian


custodian = Custodian(
    model="gpt-4o",
    system_prompt="You are a customer support agent.",
    name="Customer Support AI",
    privacy_enabled=True,
)

custodian.add_examples(
    [
        {"user": "How do I reset my password?", "assistant": "Go to settings, open security, and choose reset password."},
        {"user": "How do I invite teammates?", "assistant": "Open workspace settings, then add members by email."},
    ]
)

app = custodian.deploy()

# Chat using default model (gpt-4o)
reply = app.chat("How do I invite a new teammate?") 
if reply is not None:
    print(reply.response)
    print(reply.session_id)

# Optional: Override model for this chat request
# reply = app.chat("How do I invite a new teammate?", model="claude-3.5-sonnet")
# if reply is not None:
#     print(reply.response)