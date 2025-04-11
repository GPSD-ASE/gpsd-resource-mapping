# Decision Engine – Disaster Response Resource Allocator

This project is a modular FastAPI-based system that intelligently allocates emergency resources—fire trucks, ambulances, and police—based on incident reports submitted by users. It calculates **separate severity scores** for each service using crisp data (like number injured, radius) and an optional **fuzzy modifier** (based on incident descriptions). If any score crosses a critical threshold, the engine escalates the incident via an external **GPT-based service**.

---

##  Key Features

- Disaster-specific **severity scoring** for fire, medical, and police.
- Resource mapping tailored per service.
- Description-based fuzzy logic and environment inference.
- Separate escalation thresholds per service.
- GPT escalation service integration.
- Built using **FastAPI** (lightweight, high-performance Python framework).

---


---


### `app.py`
- FastAPI entry point
- Endpoint `/decision/incident` receives incident input, computes severity, allocates resources, and triggers escalation if needed.

---

### `config/settings.py`
- Constants for severity thresholds:
  - `fire`, `medical`, `police`
- Weights used in crisp severity scoring
- Function `radius_multiplier()` to adjust based on disaster zone size

---

### `logic/severity_calculation.py`
- Three functions:
  - `calculate_fire_severity()`
  - `calculate_medical_severity()`
  - `calculate_police_severity()`
- Combines them using `calculate_overall_severity()`

---

### `logic/fuzzy_modifier.py`
- Analyzes incident description
- Boosts or reduces severity scores using high/low keyword matches

---

### `logic/resource_mapping.py`
- `infer_environment()`: guesses location type from description
- `map_fire_resources()`, `map_medical_resources()`, `map_police_resources()`: convert scores to counts
- `map_all_resources()`: combines all three

---

### `services/gpt_escalation_service.py`
- Calls GPT escalation API if any severity score exceeds its threshold

---


