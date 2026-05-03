## 2024-05-18 - Avoid setdefault in loops
**Learning:** Using `dict.setdefault(key, default_obj)` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations and being slower.
**Action:** Replace `dict.setdefault(key, []).append(val)` with `collections.defaultdict(list)` for better performance without sacrificing readability.
