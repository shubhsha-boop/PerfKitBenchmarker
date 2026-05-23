## 2024-05-23 - Avoid dict.setdefault in hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set() `) inside a loop evaluates the default argument on every iteration, causing unnecessary memory allocations and performance overhead.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` inside hot loops to lazily initialize the default value and improve performance.
