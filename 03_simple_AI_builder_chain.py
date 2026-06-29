from custodian_labs import AssistantBuilder

#Chaining together builder methods to configure and deploy an assistant in one step. This is ideal for simple use cases and quick iterations.

app = (
    AssistantBuilder()
    .with_model("gpt-4o")
    .with_name("Finance Policy AI")
    .with_prompt("You are a helpful finance assistant.")
    .with_examples(
        [
            {"user": "When is an invoice overdue?", "assistant": "An invoice is overdue after the due date passes without payment."}
        ]
    )
    .deploy()
)

# Chat using default model (gpt-4o)
reply = app.chat("Give me a short overdue invoice policy.")
if reply is not None:
    print(reply.response)

# Optional: Override model for this chat request
# reply = app.chat("Give me a short overdue invoice policy.", model="claude-3.5-sonnet")
# if reply is not None:
#     print(reply.response)