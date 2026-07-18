## 2024-05-13 - [Avoid setdefault in hot loops]
**Learning:** Using `dict.setdefault(key, default_obj)` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations. This is a common Python performance anti-pattern.
**Action:** Replace `dict.setdefault(key, set())` with `collections.defaultdict(set)` to lazily initialize the default value, improving performance without sacrificing readability.
