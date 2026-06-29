# Custodian Labs Python Samples

Build production-ready AI-agents in 5 lines.

Example scripts for the [`custodian-labs`](https://pypi.org/project/custodian-labs/) Python SDK.

- **Docs:** https://docs.custodianlabs.io
- **Dashboard (API keys):** https://dashboard.custodianlabs.io

---

## Install

```bash
pip install custodian-labs
```

---

## Set Your API Key

Get your key from the [Dashboard](https://dashboard.custodianlabs.io) under **API Keys**.

macOS / Linux:
```bash
export CUSTODIAN_SDK_API_KEY="custodian_labs_xxxx..."
```

Windows (PowerShell):
```powershell
$env:CUSTODIAN_SDK_API_KEY = "custodian_labs_xxxx..."
```

---

## Samples

### AI Agents & Assistants

| File | What it shows |
|---|---|
| `01_simple_AI_agent_RAG.py` | Deploy a prodution-ready (+RAG) AI agent in 5 lines (not including spaces) |
| `02_simple_AI_few_shot_learning.py` | Add few-shot examples to guide the assistant's responses |
| `03_simple_AI_builder_chain.py` | Fluent `AssistantBuilder` chain — configure and deploy in one expression |
| `04_AI_agent_application_example.py` | Production-style example: Legal assistant with a PDF knowledge base |
| `05_simple_multi_agent.py` | Multi-agent team with topic-based routing (`AgentTeam`) |

### GuardianLayer — PII & Proprietary Data Masking

| File | What it shows |
|---|---|
| `guardian_layer_examples/06_simple_guardian_layer_text.py` | Analyze text for sensitive words and de-identify inline |
| `guardian_layer_examples/07_simple_guardian_layer_file.py` | De-identify a CSV file and return the masked file |

### WebSocket Bridge

| File | What it shows |
|---|---|
| `websocket_examples/08_simple_websocket_bridge.py` | FastAPI WebSocket server that proxies chat through the SDK |
| `websocket_examples/09_simple_websocket_browser.html` | Browser client for the WebSocket bridge |

---

## Running a Sample

Run any script from the **repo root** (so that `data_examples/` paths resolve correctly):

macOS / Linux:
```bash
python 01_simple_AI_agent_live.py
```

Windows (PowerShell):
```powershell
python 01_simple_AI_agent_live.py
```

**WebSocket sample** — requires `fastapi` and `uvicorn`:

```bash
pip install fastapi uvicorn
uvicorn websocket_examples.08_simple_websocket_bridge:app --reload
```

Then open `websocket_examples/09_simple_websocket_browser.html` in a browser.

---

## SDK Quick Reference

**Single assistant (high-level)**
```python
from custodian_labs import Custodian

app = Custodian(model="gpt-4o", system_prompt="You are a helpful assistant.")
app.add_data_source_file("data_examples/car_info.csv")
deployed = app.deploy()

reply = deployed.chat("What cars are available?")
print(reply.response)
```

**One-liner fast path**
```python
from custodian_labs import create_assistant

app = create_assistant(model="gpt-4o", prompt="You are a helpful assistant.")
reply = app.chat("Hello!")
print(reply.response)
```

**Multi-agent team**
```python
from custodian_labs import Agent, AgentTeam

team = AgentTeam(
    agents=[
        Agent(name="billing", model="gpt-4o", system_prompt="Handle billing.", topics=["billing"]),
        Agent(name="support", model="gpt-4o", system_prompt="Handle support.", topics=["support"]),
    ],
    routing_mode="single",
)
app = team.deploy()
reply = app.chat("I have a question about my invoice.")
print(reply.response, reply.selected_agent)
```

**PII masking**
```python
from custodian_labs import GuardianLayer

guardian = GuardianLayer()

# Text
outputs = guardian.deidentify_text_outputs("John Smith, 617-555-0100", masking_type="redact")
for item in outputs.outputs:
    print(item.text)

# File (auto-dispatches by extension: csv, docx, pdf, txt)
result = guardian.deidentify_file("data_examples/pii_data.csv", masking_type="transform")
print(result.text())
```

---

## Environment Variables

| Variable | Default | Purpose |
|---|---|---|
| `CUSTODIAN_SDK_API_KEY` | — | API key for all assistant/agent calls |
| `CUSTODIAN_SDK_BASE_URL` | `https://platform.custodianlabs.io/v1` | Override the assistant API host |
| `CUSTODIAN_MASKING_BASE_URL` | `https://privacy.custodianlabs.io` | Override the masking API host |
