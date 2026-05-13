## 2024-05-24 - Python dict.setdefault in Hot Loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace `setdefault` with `collections.defaultdict` inside hot loops for lazy initialization of default values, resulting in up to 2x speedup in the loop.
