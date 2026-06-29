from custodian_labs import GuardianLayer


guardian = GuardianLayer()

result = guardian.deidentify_file(
    "data_examples/pii_data.csv",
    masking_type="transform",
    pii_entities=["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER"],
)

print(result.filename)
print(result.media_type)
print(result.text())