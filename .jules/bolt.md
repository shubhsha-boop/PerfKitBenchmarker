## 2026-09-30 - Optimize Hot Path Dictionary Formatting
**Learning:** In hot serialization paths (like sample metadata processing), replacing traditional loops utilizing `.append()` and `%` string formatting with list comprehensions and f-strings yields measurable performance speedups.
**Action:** Always favor list comprehensions with f-strings for building string arrays from dictionaries in high-frequency serialization code.
