import json
import datetime
import os

file_path = "database/solana.json"

if not os.path.exists(file_path):
    data = {
        "network": "Solana",
        "scam_tokens": []
    }
else:
    with open(file_path, "r") as f:
        data = json.load(f)

new_token = {
    "name": "Example Scam Token",
    "symbol": "SCAM",
    "address": "ExampleAddress123",
    "type": "Impersonation",
    "status": "Active",
    "first_detected": str(datetime.date.today()),
    "reported_by": "crypto-security-research",
    "description": "Automatically detected scam token example."
}

data["scam_tokens"].append(new_token)

with open(file_path, "w") as f:
    json.dump(data, f, indent=2)

print("Database updated successfully")
