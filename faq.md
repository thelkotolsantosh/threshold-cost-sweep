# FAQ

## 1. What does it select?

A single cutoff for a binary classifier.

## 2. What problem motivates it?

A default cutoff can generate expensive missed errors.

## 3. Who might use it?

A QA analyst tuning which invoices go to manual review.

## 4. What decisions can it compare?

Every distinct observed score and the rule that flags nothing.

## 5. Which language is required?

Python 3.10 or newer runs the command and tests.

## 6. Which dependencies are needed?

CSV parsing, counting and JSON serialization use the standard library.

## 7. Does it require a GPU?

No. The sorted sweep runs on a CPU.

## 8. How do I install it?

Clone the repository and open the directory containing sweep.py.

## 9. How do I set the costs?

Use --fp-cost for false alarms and --fn-cost for misses in the same units.

## 10. How do I run the sample?

Run python sweep.py examples/sample.csv --fn-cost 5.

## 11. Where are the files?

sweep.py implements the algorithm, examples holds sample scores and tests holds regression cases.

## 12. How are tied scores handled?

All observations with an identical score change prediction together.

## 13. Which columns are required?

Supply score and label with those lowercase headers.

## 14. What does null mean?

The cheapest selected rule classifies every row as negative.

## 15. Can I use fractional costs?

Scale both costs to a common integer unit before running.

## 16. What happens on invalid input?

The CLI prints an input error to stderr and exits with status 2.

## 17. Why did a score of 85 fail?

Use a normalized score such as 0.85 for an 85 percent prediction.

## 18. How do I reproduce a result?

Keep the exact scored CSV and both cost flags with the experiment.

## 19. How do I run tests?

Run python -m unittest discover -s tests -v from the repository root.

## 20. How can I contribute?

Provide an input and expected confusion counts illustrating the requested behavior.

## 21. Can it train a model?

It consumes scores produced by a separate classifier.

## 22. Can the cutoff go straight into production?

Evaluate it on untouched representative data and check review capacity first.

## 23. What extension would help?

Bootstrap intervals could show how sensitive the cutoff is to the validation sample.

## 24. How do I protect invoice data?

Export only scores and binary outcomes and keep private CSVs outside the repository.

## 25. Where is the worked result?

README.md walks through the example and explains its one-unit cost.

