## 2024-05-24 - Avoid setdefault in Python Hot Loops
**Learning:** Using `dict.setdefault(key, default_obj)` inside a hot loop evaluates the `default_obj` argument (like `set()` or `[]`) on every iteration, leading to unnecessary memory allocations and performance degradation.
**Action:** Replace `setdefault` with `collections.defaultdict(type)` when lazily initializing collections inside loops to improve execution speed and reduce overhead.
