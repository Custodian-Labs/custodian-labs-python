# Simple SDK Samples

This folder contains very simple examples for customers using the SDK.

## Install First

Create and activate a virtual environment from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If you want to run these samples against the published SDK:

```powershell
pip install custodian-labs
```

If you are running the samples from this repository while developing locally, install the SDK from the repo root instead:

```powershell
pip install -e .
```

## Set Environment Variables

Set your environment first.

For assistant and agent samples:

```powershell
$env:CUSTODIAN_SDK_API_KEY="your-api-key"
```

For GuardianLayer masking samples:

```powershell
$env:CUSTODIAN_SDK_API_KEY="your-api-key"
```

`GuardianLayer()` now defaults to `https://privacy.custodianlabs.io`, so you only need to set `CUSTODIAN_MASKING_BASE_URL` if you want to override that host.

`Assistant`, `Agent`, and `create_assistant()` already default to the production platform endpoint, so you only need `CUSTODIAN_SDK_BASE_URL` if you want to override the host.

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

## Run A Sample

From the repository root:

```powershell
python git_samples\01_simple_assistant_cmd.py
```

Run the CSV-based examples from inside the `git_samples` folder so the sample file path works exactly as written:

```powershell
cd git_samples
python 01_simple_assistant_cmd.py
```