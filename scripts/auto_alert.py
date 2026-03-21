import json
from datetime import datetime

ALERTS_FILE = "alerts/alerts.json"

def load_alerts():
    try:
        with open(ALERTS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_alerts(alerts):
    with open(ALERTS_FILE, "w") as f:
        json.dump(alerts, f, indent=2)

def create_alert(address):
    alerts = load_alerts()

    new_alert = {
        "id": f"ARTA-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
        "title": "Suspicious Token Detected",
        "description": f"New suspicious token detected: {address}",
        "risk_level": "MEDIUM",
        "chain": "solana",
        "address": address,
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "status": "active"
    }

    alerts.append(new_alert)
    save_alerts(alerts)

if __name__ == "__main__":
    # ТЕСТ (потом заменим на реальные данные)
    create_alert("AUTO_TEST_TOKEN")
