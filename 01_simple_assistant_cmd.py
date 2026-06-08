from custodian_labs import Custodian


custodian = Custodian(
    model="gpt-4o",
    system_prompt="You are a helpful assistant, and you are given a data file to answer questions about the data.",
    privacy_enabled=False,
)

custodian.add_data_source_file("sample_pii_data.csv")

app = custodian.deploy()

print("CMD chat is ready. Type your message and press Enter.")
print(app.chat_url)
print("Type 'exit' (or 'quit') to stop.\n")

result = app.chat()
print(result)