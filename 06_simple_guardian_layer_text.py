from custodian_labs import GuardianLayer


guardian = GuardianLayer()

text = "John Smith lives in Boston and his phone number is 617-555-0100."

analysis = guardian.analyze_proprietary(text)
print("Sensitive words:")
print(analysis.sensitive_words)

outputs = guardian.deidentify_text_outputs(
    text,
    masking_type="redact",
    pii_entities=["ALL"],
)

for item in outputs.outputs:
    print(item.id, item.text)