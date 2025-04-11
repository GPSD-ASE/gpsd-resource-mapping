
def infer_environment(description: str) -> str:
    if not description:
        return "Urban"

    description = description.lower()

    if "industrial" in description or "factory" in description or "warehouse" in description:
        return "Industrial"
    elif "residential" in description or "apartment" in description or "housing" in description:
        return "Residential"
    elif "stadium" in description or "arena" in description:
        return "Stadium"
    elif "school" in description or "college" in description:
        return "Educational"
    else:
        return "Urban"

def map_fire_resources(data, fire_score: float) -> dict:
    if data["incidentType"].lower() != "fire":
        return {"fire_truck": 0}

    env = infer_environment(data.get("description", ""))
    base = 2 if fire_score < 10 else 4 if fire_score < 20 else 6

    result = {"fire_truck": base}

 

    return result

def map_medical_resources(data, medical_score: float) -> dict:
    num_injured = data.get("numInjured", 0)
    if num_injured == 0:
        return {"ambulance": 0}

    base = 1 if medical_score < 10 else 2 if medical_score < 20 else 3
    extra = max(1, num_injured // 10)

    return {"ambulance": base + extra}

def map_police_resources(data, police_score: float) -> dict:
    base = 2 if police_score < 10 else 5 if police_score < 20 else 10
    return {"police": base}

def map_all_resources(data, scores: dict) -> dict:
    fire = map_fire_resources(data, scores["fire"])
    medical = map_medical_resources(data, scores["medical"])
    police = map_police_resources(data, scores["police"])

    combined = {}
    combined.update(fire)
    combined.update(medical)
    combined.update(police)

    return combined
