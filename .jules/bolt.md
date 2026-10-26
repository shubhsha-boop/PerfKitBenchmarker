## 2026-10-26 - Optimize Metadata Formatting
**Learning:** Python Performance Insight: When serializing dictionaries to JSON-like strings with specific spacing requirements, using `json.dumps(obj, separators=(',', ': '))` is significantly faster (~20%+) than manually constructing the string via iteration loops and `join()`. Note that `json.dumps` automatically stringifies numeric keys (e.g., floats), ensuring output format parity with manual f-string formatting.
**Action:** Use `json.dumps(..., separators=...)` for dictionary serialization in hot paths when format matches.
