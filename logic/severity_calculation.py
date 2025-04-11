from config.settings import CRISP_WEIGHTS, radius_multiplier

def calculate_fire_severity(data, fuzzy_modifier=1.0):
    # For fire incidents, use the incidentType weight (3 for Fire, else 1).
    base = CRISP_WEIGHTS["incidentType"].get(data["incidentType"], 1)
    injured = data.get("numInjured", 0)
    affected = data.get("numAffected", 0)
    radius = data.get("radius", 100)
    crisp = base + injured * CRISP_WEIGHTS["numInjured"] + affected * CRISP_WEIGHTS["numAffected"]
    return crisp * radius_multiplier(radius) * fuzzy_modifier

def calculate_medical_severity(data, fuzzy_modifier=1.0):
    injured = data.get("numInjured", 0)
    radius = data.get("radius", 100)
    base = 1
    crisp = base + injured * 1.0
    return crisp * radius_multiplier(radius) * fuzzy_modifier

def calculate_police_severity(data, fuzzy_modifier=1.0):
    affected = data.get("numAffected", 0)
    radius = data.get("radius", 100)
    base = 1
    crisp = base + affected * 0.8
    return crisp * radius_multiplier(radius) * fuzzy_modifier

def calculate_overall_severity(data, fuzzy_modifier=1.0):
    fire = calculate_fire_severity(data, fuzzy_modifier)
    medical = calculate_medical_severity(data, fuzzy_modifier)
    police = calculate_police_severity(data, fuzzy_modifier)
    overall = max(fire, medical, police)
    return overall, {"fire": fire, "medical": medical, "police": police}
