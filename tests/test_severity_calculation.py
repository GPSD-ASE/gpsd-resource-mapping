import unittest
from logic.severity_calculation import (
    calculate_fire_severity,
    calculate_medical_severity,
    calculate_police_severity,
    calculate_overall_severity
)

class TestSeverityCalculation(unittest.TestCase):
    def test_fire_severity_low(self):
        data = {
            "incidentType": "Fire",
            "numInjured": 0,
            "numAffected": 0,
            "radius": 50
        }
        score = calculate_fire_severity(data, fuzzy_modifier=1.0)
        self.assertGreater(score, 0)

    def test_fire_severity_medium(self):
        data = {
            "incidentType": "Fire",
            "numInjured": 10,
            "numAffected": 50,
            "radius": 300
        }
        score = calculate_fire_severity(data, fuzzy_modifier=1.0)
        self.assertTrue(score > 10)

    def test_medical_severity(self):
        data = {
            "incidentType": "Accident",
            "numInjured": 30,
            "numAffected": 20,
            "radius": 250
        }
        score = calculate_medical_severity(data, fuzzy_modifier=1.0)
        self.assertTrue(score > 0)

    def test_police_severity(self):
        data = {
            "incidentType": "Accident",
            "numInjured": 5,
            "numAffected": 80,
            "radius": 400
        }
        score = calculate_police_severity(data, fuzzy_modifier=1.0)
        self.assertTrue(score > 0)

    def test_overall_severity_increase_with_radius(self):
        data = {
            "incidentType": "Fire",
            "numInjured": 20,
            "numAffected": 100,
            "radius": 400
        }
        overall1, _ = calculate_overall_severity(data, fuzzy_modifier=1.0)
        data["radius"] = 1000
        overall2, _ = calculate_overall_severity(data, fuzzy_modifier=1.0)
        self.assertTrue(overall2 > overall1)

if __name__ == "__main__":
    unittest.main()
