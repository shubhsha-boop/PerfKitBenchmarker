## 2026-09-02 - [Optimize setdefault in hot loop]
**Learning:** Using `dict.setdefault(key, default_obj)` like `set()` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with `collections.defaultdict` as it lazily initializes the default value, improving performance.
