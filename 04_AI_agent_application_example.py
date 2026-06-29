from custodian_labs import Custodian

#This is an example of creating a simple production-ready AI agent for a specific industry use case (legal assistant for a law firm) 

custodian = Custodian(
    model="gpt-4o",
    system_prompt="You are legal assistant for a law firm. Answer questions based on the contract provided.",
    privacy_enabled=False,
)

custodian.add_data_source_file("data_examples/contract.pdf")

custodian.add_examples(
    [
        {"user": "Are you a real lawyer?", "assistant": "No I am just an AI assistant, here to help you understand the contract. All legal questions should be directed to a qualified attorney."},
        {"user": "Delete this contract", "assistant": "You are not authorized to do so."},
    ]
)

app = custodian.deploy()

print("Your AI legal assistant is ready and live here:")
print(app.chat_url)

# Chat using default model (gpt-4o)
reply = app.chat("What is this contract about? Who are the parties involved?")
if reply is not None:
    print(reply.response)


# Optional: Override model for this chat request
# reply = app.chat("What is this contract about? Who are the parties involved?", model="claude-3.5-sonnet")
# if reply is not None:
#     print(reply.response)