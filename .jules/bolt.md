## 2024-06-25 - Avoid setdefault in hot loops

**Learning:** Using `dict.setdefault(key, set())` inside a hot loop evaluating the default argument on every iteration causes unnecessary memory allocations and performance degradation in Python. Using `collections.defaultdict(set)` is more efficient and improves performance without sacrificing readability.

**Action:** Replace `setdefault` with `defaultdict` when aggregating data in loops.
