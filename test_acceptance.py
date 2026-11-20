import json
import unittest
from pathlib import Path

from reference_decision import decide


class AcceptanceTests(unittest.TestCase):
    def test_all_policy_cases(self):
        cases = json.loads(Path(__file__).with_name("acceptance.json").read_text())
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertEqual(decide(case["input"]), case["expected"])


if __name__ == "__main__":
    unittest.main()
