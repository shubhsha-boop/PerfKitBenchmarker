## 2026-10-24 - Optimize Sample Serialization in InfluxDB Publisher
**Learning:** In hot serialization paths for formatting key-value tags (e.g., sample metadata processing), replacing traditional loops utilizing `.append()` and `%` string formatting with list comprehensions and f-strings yields measurable (~15%+) performance speedups.
**Action:** Prioritize list comprehensions and f-strings when transforming dictionaries into a list of strings, checking explicitly for empty string cases (`v == ''`).
