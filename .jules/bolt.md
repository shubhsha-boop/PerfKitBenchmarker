## 2024-05-24 - Avoid setdefault in hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` like `set()` or `[]` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` to lazily initialize the default value, improving performance without sacrificing readability.
