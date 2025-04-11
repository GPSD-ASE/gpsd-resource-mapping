import unittest
from logic.fuzzy_modifier import compute_fuzzy_modifier

class TestFuzzyModifier(unittest.TestCase):
    def test_empty_description(self):
        self.assertEqual(compute_fuzzy_modifier(""), 1.0)
        self.assertEqual(compute_fuzzy_modifier(None), 1.0)

    def test_single_high_keyword(self):
        self.assertAlmostEqual(compute_fuzzy_modifier("catastrophic"), 1.2)
        self.assertAlmostEqual(compute_fuzzy_modifier("severe"), 1.2)

    def test_multiple_high_keywords(self):
        self.assertAlmostEqual(compute_fuzzy_modifier("catastrophic explosive"), 1.4)

    def test_single_low_keyword(self):
        self.assertAlmostEqual(compute_fuzzy_modifier("minor"), 0.9)
        self.assertAlmostEqual(compute_fuzzy_modifier("small"), 0.9)

    def test_combined_keywords(self):
        self.assertAlmostEqual(compute_fuzzy_modifier("catastrophic minor"), 1.1)
        self.assertAlmostEqual(compute_fuzzy_modifier("small limited"), 0.8)

if __name__ == "__main__":
    unittest.main()
