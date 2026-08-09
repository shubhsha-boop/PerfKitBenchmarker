## 2024-08-09 - Avoid dict.setdefault with mutable defaults in loops
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations and degrading performance.
**Action:** Replace `dict.setdefault(..., default_obj)` with `collections.defaultdict(default_type)` for lazy initialization in hot loops to avoid redundant instantiations.
