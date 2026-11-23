"""Find the least-cost binary decision rule on labeled validation scores."""
import argparse
import csv
import json
from collections import Counter


def choose(rows, fp_cost=1, fn_cost=1):
    if min(fp_cost, fn_cost) < 0:
        raise ValueError("Costs must be nonnegative")
    counts = Counter()
    for row in rows:
        score = float(row["score"])
        label = row["label"]
        if not 0 <= score <= 1 or label not in ("0", "1"):
            raise ValueError("Expected a score in [0, 1] and label 0 or 1")
        counts[score, int(label)] += 1
    if not counts:
        raise ValueError("Expected at least one validation row")
    misses = sum(n for (_, label), n in counts.items() if label)
    alarms = 0
    best = dict(threshold=None, cost=misses * fn_cost, fp=0, fn=misses)
    for score in sorted({s for s, _ in counts}, reverse=True):
        alarms += counts[score, 0]
        misses -= counts[score, 1]
        cost = alarms * fp_cost + misses * fn_cost
        if cost < best["cost"]:
            best = dict(threshold=score, cost=cost, fp=alarms, fn=misses)
    return best


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file")
    parser.add_argument("--fp-cost", type=int, default=1)
    parser.add_argument("--fn-cost", type=int, default=1)
    args = parser.parse_args()
    try:
        with open(args.csv_file, newline="", encoding="utf-8-sig") as source:
            print(json.dumps(choose(csv.DictReader(source), args.fp_cost, args.fn_cost)))
    except (OSError, ValueError, KeyError, TypeError, csv.Error) as error:
        parser.exit(2, f"Invalid input: {error}\n")
