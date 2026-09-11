## 2026-09-11 - Use defaultdict instead of dict.setdefault in hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` to lazily initialize the default value and improve performance.
