## 2024-05-18 - Avoid dict.setdefault with mutable defaults in hot loops
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop evaluates the default argument (creating a new `set`) on every iteration, causing unnecessary memory allocations and degrading performance.
**Action:** Replace `dict.setdefault` with `collections.defaultdict(set)` to lazily initialize the default value without evaluating it unnecessarily.
