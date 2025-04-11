SEVERITY_THRESHOLDS = {
    "fire": 20,       # If fire severity exceeds 20, escalate for fire services.
    "medical": 18,    # If medical severity exceeds 18, escalate for ambulances.
    "police": 15      # If police severity exceeds 15, escalate for police.
}

GPT_ESCALATION_URL = "http://localhost:7000"  # (Not used anymore)

CRISP_WEIGHTS = {
    "incidentType": {
        "Fire": 3,
        "Flood": 4,
        "Accident": 2,
        "Other": 1
    },
    "numInjured": 0.5,
    "numAffected": 0.3
}

def radius_multiplier(radius_m):
    if radius_m < 100:
        return 1.0
    elif radius_m < 500:
        return 1.3
    else:
        return 1.5
