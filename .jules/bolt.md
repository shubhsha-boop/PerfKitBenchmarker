## 2024-07-28 - Optimize setdefault in tight loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations. This is a common Python performance anti-pattern.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` for lazy initialization in hot paths to avoid redundant memory allocation.
