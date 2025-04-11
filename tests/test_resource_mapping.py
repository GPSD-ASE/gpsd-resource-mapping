import unittest
from logic.resource_mapping import map_all_resources

class TestResourceMapping(unittest.TestCase):
    def test_fire_incident(self):
        data = {
            "incidentType": "Fire",
            "numInjured": 25,
            "numAffected": 120,
            "radius": 600,
            "description": "Massive fire in industrial warehouse"
        }
        scores = {"fire": 22, "medical": 20, "police": 18}
        resources = map_all_resources(data, scores)
        self.assertIn("fire_truck", resources)
        self.assertIn("ambulance", resources)
        self.assertIn("police", resources)

    def test_non_fire_incident(self):
        data = {
            "incidentType": "Accident",
            "numInjured": 15,
            "numAffected": 80,
            "radius": 400,
            "description": "Multiple vehicle collision on highway"
        }
        scores = {"fire": 5, "medical": 16, "police": 17}
        resources = map_all_resources(data, scores)
        self.assertEqual(resources.get("fire_truck", 0), 0)
        self.assertIn("ambulance", resources)
        self.assertIn("police", resources)

    def test_zero_injuries(self):
        data = {
            "incidentType": "Accident",
            "numInjured": 0,
            "numAffected": 50,
            "radius": 200,
            "description": "Minor collision"
        }
        scores = {"fire": 3, "medical": 2, "police": 4}
        resources = map_all_resources(data, scores)
        self.assertEqual(resources.get("ambulance", -1), 0)

    def test_boundary_values(self):
        data = {
            "incidentType": "Fire",
            "numInjured": 10,
            "numAffected": 50,
            "radius": 300,
            "description": "Moderate fire with some smoke"
        }
        scores_low = {"fire": 9.9, "medical": 9.9, "police": 9.9}
        resources_low = map_all_resources(data, scores_low)
        self.assertEqual(resources_low.get("fire_truck", 0), 2)

        scores_mid = {"fire": 10.0, "medical": 10.0, "police": 10.0}
        resources_mid = map_all_resources(data, scores_mid)
        self.assertEqual(resources_mid.get("fire_truck", 0), 4)

if __name__ == "__main__":
    unittest.main()
