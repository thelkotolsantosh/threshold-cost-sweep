# Threshold Cost Sweep

A billing QA team can flag an invoice when its model score reaches a cutoff. A missed error and an unnecessary review can have different costs. This offline evaluator finds the cutoff with the lowest total error cost on a labeled validation set.

## Run the example

Clone the repository and open its directory. Python 3.10+ includes all dependencies.

    python sweep.py examples/sample.csv --fp-cost 1 --fn-cost 5

The four synthetic invoices yield a cutoff of 0.4, one false alarm, zero misses and a total cost of 1. Scores equal to the cutoff count as positive.

## Inputs and algorithm

Provide a UTF-8 CSV with score and label columns. Scores must be finite and between zero and one. Labels are 0 or 1. Both cost flags accept nonnegative integers and default to one. Use a common unit such as minutes of review.

sweep.py groups equal scores, sorts the groups in descending order and updates the two error counts after each group. The initial rule flags nothing (JSON null). Ties favor fewer alerts. For n rows and u distinct scores the runtime is O(n + u log u) and memory is O(u).

## Verification and scope

Run python -m unittest discover -s tests -v. The tests cover invalid input, tied scores and endpoint decisions. Keep sensitive invoice details out of shared examples. Select a threshold on validation data and measure its performance on separate held-out data before deployment. Future work could report uncertainty by resampling invoices.

See faq.md for interpretation, CONTRIBUTING.md for changes and LICENSE for MIT terms.
