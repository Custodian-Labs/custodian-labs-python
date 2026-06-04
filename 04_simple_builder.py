from custodian_labs import AssistantBuilder


app = (
    AssistantBuilder()
    .with_model("gpt-4o")
    .with_prompt("You are a helpful finance assistant.")
    .with_examples(
        [
            {"user": "When is an invoice overdue?", "assistant": "An invoice is overdue after the due date passes without payment."}
        ]
    )
    .deploy()
)

reply = app.chat("Give me a short overdue invoice policy.")
if reply is not None:
    print(reply.response)