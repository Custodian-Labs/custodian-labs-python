# Simple SDK Samples

This folder contains very simple examples for customers using the SDK.

Set your environment first.

For assistant and agent samples:

```powershell
$env:CUSTODIAN_SDK_BASE_URL="https://platform.custodianlabs.io/v1"
$env:CUSTODIAN_SDK_API_KEY="your-api-key"
```

For GuardianLayer masking samples:

```powershell
$env:CUSTODIAN_MASKING_BASE_URL="https://your-masking-api-host"
$env:CUSTODIAN_SDK_API_KEY="your-api-key"
```

Files in this folder:

- `01_simple_assistant_cmd.py`
- `02_simple_assistant_with_examples.py`
- `03_simple_create_assistant.py`
- `04_simple_builder.py`
- `05_simple_multi_agent.py`
- `06_simple_guardian_layer_text.py`
- `07_simple_guardian_layer_file.py`
- `08_simple_websocket_bridge.py`
- `09_simple_websocket_browser.html`
- `sample_pii_data.csv`

Run the CSV-based examples from inside the `git_samples` folder so the sample file path works exactly as written:

```powershell
cd git_samples
python 01_simple_assistant_cmd.py
```