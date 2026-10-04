## 2026-10-04 - Optimize GetLabelsFromDict serialization
**Learning:** In hot serialization paths (like sample metadata processing), replacing traditional loops utilizing `.append()` and `%` string formatting with list comprehensions and f-strings (e.g., `','.join([f'{k}:{v}' for k, v in dict.items()])`) yields measurable performance speedups.
**Action:** Always prefer list comprehensions and f-strings for string concatenation over loops with `.append()` and `%` formatting when serializing dictionaries, especially in performance-critical code paths.
