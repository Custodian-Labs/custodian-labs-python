from custodian_labs import Agent, AgentTeam


team = AgentTeam(
    agents=[
        Agent(
            name="billing",
            model="gpt-4o",
            system_prompt="Answer billing questions.",
            topics=["billing", "invoice", "refund", "payment"],
        ),
        Agent(
            name="data",
            model="gpt-4o",
            system_prompt="Answer questions about the uploaded CSV file.",
            topics=["data", "csv", "customer", "file"],
        ).add_data_source_file("sample_pii_data.csv"),
    ],
    routing_mode="single",
)

app = team.deploy()

# Chat using agents' default models (gpt-4o)
reply = app.chat("How many people are in the uploaded file and which cities do they live in?")
if reply is not None:
    print(reply.response)
    print(reply.selected_agent)

# Optional: Override model for this chat request
# reply = app.chat("How many people are in the uploaded file and which cities do they live in?", model="claude-3.5-sonnet")
# if reply is not None:
#     print(reply.response)
#     print(reply.selected_agent)