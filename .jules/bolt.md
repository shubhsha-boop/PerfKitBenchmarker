## 2024-05-28 - Avoid setdefault in hot loops
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with `collections.defaultdict(set)` to lazily initialize the default value, improving performance without sacrificing readability.
