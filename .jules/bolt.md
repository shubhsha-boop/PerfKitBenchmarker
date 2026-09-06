## 2026-09-06 - Optimize loop performance by replacing setdefault with defaultdict
**Learning:** Using `dict.setdefault(key, default_obj)` like `set()` inside a loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace `setdefault` with `collections.defaultdict` to lazily initialize default values in hot loops.
