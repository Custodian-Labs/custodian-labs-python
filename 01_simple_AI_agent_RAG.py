from custodian_labs import Custodian

custodian = Custodian(
    model="gpt-4o",
    system_prompt="You are a helpful assistant, and you are given a data file to answer questions about the data.",
    name="PII Data Assistant",
    privacy_enabled=False,
)

custodian.add_data_source_file("data_examples/car_info.csv")

app = custodian.deploy()

print("Your AI agent is ready and live here:")
print(app.chat_url)

# Test your agent on the command line:
print("CMD chat is ready. Type your message and press Enter.")
print("Type 'exit' (or 'quit') to stop.\n")
result = app.chat()
print(result)

# Tip: You can also pass a model parameter to chat() for non-interactive requests
# result = app.chat("Your message here", model="claude-3.5-sonnet")
# result = app.chat()
# print(result)

