## 2024-05-24 - Avoid dict.setdefault inside loops
**Learning:** Using `dict.setdefault(k, set())` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace `dict.setdefault` with `collections.defaultdict(set)` inside loops to avoid creating unused default objects and improve performance.
