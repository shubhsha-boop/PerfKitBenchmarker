## 2024-10-05 - Serialization Loop Performance Optimization
**Learning:** In hot serialization paths (like sample metadata processing), replacing traditional loops utilizing `.append()` and `%` string formatting with list comprehensions and f-strings (e.g., `[f'{k}:{v}' for k, v in dict.items()]`) yields measurable performance speedups.
**Action:** Always prefer list comprehensions and f-strings for simple transformations of iterables into lists of strings, particularly in code paths dealing with metrics serialization.
