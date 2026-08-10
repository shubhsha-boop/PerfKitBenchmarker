## 2024-08-10 - Avoid dict.setdefault in hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()` or `[]`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` for lazy initialization when populating collections in high-frequency code paths.
