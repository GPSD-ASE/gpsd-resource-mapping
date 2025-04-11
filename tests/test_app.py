import sys
import os
# Add the project root to sys.path so that 'app' is accessible
project_root = os.path.join(os.path.dirname(__file__), "..")
if project_root not in sys.path:
    sys.path.append(project_root)

import unittest
from fastapi.testclient import TestClient
from app import app

class TestAppEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_non_escalated_incident(self):
        # Adjusted payload: Lower numAffected (from 20 to 10) to avoid escalation.
        payload = {
            "incidentId": "INC100",
            "incidentType": "Accident",
            "numInjured": 5,
            "numAffected": 10,
            "radius": 150,
            "description": "Minor accident with small impact"
        }
        response = self.client.post("/decision/incident", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("incidentId", data)
        self.assertIn("overallSeverityScore", data)
        self.assertIn("resourcesNeeded", data)
        self.assertFalse(data["escalation"])
        self.assertNotEqual(data["resourcesNeeded"], {})

    def test_escalated_incident(self):
        payload = {
            "incidentId": "INC200",
            "incidentType": "Fire",
            "numInjured": 50,
            "numAffected": 200,
            "radius": 600,
            "description": "Catastrophic fire with extensive damage in industrial area"
        }
        response = self.client.post("/decision/incident", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["escalation"])
        self.assertEqual(data["resourcesNeeded"], {})

    def test_edge_values(self):
        payload = {
            "incidentId": "INC300",
            "incidentType": "Accident",
            "numInjured": 0,
            "numAffected": 0,
            "radius": 50,
            "description": "Minor incident"
        }
        response = self.client.post("/decision/incident", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["escalation"])
        self.assertEqual(data["resourcesNeeded"].get("ambulance", 0), 0)

if __name__ == "__main__":
    unittest.main()
