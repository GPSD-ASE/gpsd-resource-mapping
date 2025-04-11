from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, Dict

from logic.severity_calculation import calculate_overall_severity
from logic.fuzzy_modifier import compute_fuzzy_modifier
from logic.resource_mapping import map_all_resources
from config.settings import SEVERITY_THRESHOLDS

app = FastAPI(title="Decision Engine")

class IncidentInput(BaseModel):
    incidentId: str
    incidentType: str
    numInjured: int = Field(..., ge=0)
    numAffected: int = Field(..., ge=0)
    radius: float = Field(..., gt=0)
    description: Optional[str] = None

class DecisionOutput(BaseModel):
    incidentId: str
    overallSeverityScore: float
    individualSeverityScores: Dict[str, float]
    resourcesNeeded: Dict[str, int]
    escalation: bool

@app.post("/decision/incident", response_model=DecisionOutput)
def decide_incident(incident: IncidentInput):
    fuzzy_mod = compute_fuzzy_modifier(incident.description)
    incident_data = incident.dict()
    overall_score, scores = calculate_overall_severity(incident_data, fuzzy_modifier=fuzzy_mod)
    escalation_flags = {
        "fire": scores["fire"] >= SEVERITY_THRESHOLDS["fire"],
        "medical": scores["medical"] >= SEVERITY_THRESHOLDS["medical"],
        "police": scores["police"] >= SEVERITY_THRESHOLDS["police"]
    }
    should_escalate = any(escalation_flags.values())
    
    
    resources_needed = {} if should_escalate else map_all_resources(incident_data, scores)
    
    return DecisionOutput(
        escalation=should_escalate,
        incidentId=incident.incidentId,
        overallSeverityScore=overall_score,
        individualSeverityScores=scores,
        resourcesNeeded=resources_needed,
        
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
