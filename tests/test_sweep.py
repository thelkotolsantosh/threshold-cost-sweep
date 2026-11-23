import unittest
from sweep import choose


class Rules(unittest.TestCase):
    def test_equal_scores_move_together(self):
        rows = [dict(score=".5", label=i) for i in ["0", "1"]]
        self.assertIsNone(choose(rows)["threshold"])
        self.assertEqual(choose(rows, fn_cost=2), dict(threshold=.5, cost=1, fp=1, fn=0))

    def test_endpoint(self):
        self.assertEqual(choose([dict(score="0", label="1")])["threshold"], 0)

    def test_invalid(self):
        for rows in [[], [dict(score="nan", label="1")], [dict(score=".1", label="2")]]:
            with self.assertRaises(ValueError):
                choose(rows)
