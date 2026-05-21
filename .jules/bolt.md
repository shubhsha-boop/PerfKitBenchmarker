## 2024-05-24 - Python `dict.setdefault` in nested loop
**Learning:** `dict.setdefault(k, set())` inside a hot loop is an anti-pattern. Eager argument evaluation causes a new empty `set()` to be allocated and garbage-collected on every iteration if the key exists, significantly impacting iteration performance over large datasets.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` for nested loops or high-frequency iteration where lazy initialization of default complex objects (like `list`, `dict`, or `set`) avoids redundant memory allocations.
