## 2026-09-04 - Optimize dict.setdefault with collections.defaultdict
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations. Replacing it with `collections.defaultdict` lazy initializes the default value, improving performance.
**Action:** Use `collections.defaultdict(set)` instead of `dict.setdefault(key, set())` in performance-critical loops to avoid redundant object allocations.
