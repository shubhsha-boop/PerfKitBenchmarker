## 2024-05-24 - Defaultdict vs Setdefault
**Learning:** Using `dict.setdefault(key, default_obj)` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace `setdefault` with `collections.defaultdict` for lazily initializing default values, improving performance without sacrificing readability.
