## 2024-05-24 - Python `dict.setdefault` inside hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` where `default_obj` is a newly instantiated object (like `set()`, `[]`, or `{}`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations and degrading performance.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` to lazily initialize the default value and avoid redundant instantiations inside loops.
