## 2024-05-24 - Avoid setdefault in hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations and slowdowns (e.g., allocating a new `set()` thousands of times).
**Action:** Replace `setdefault` with `collections.defaultdict` for lazy initialization, which is about 25% faster in metadata processing loops.
