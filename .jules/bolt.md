## 2025-02-12 - Avoid dict.setdefault in hot loops
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop evaluates the default argument `set()` on every iteration, causing unnecessary memory allocations.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` to lazily initialize the default value, improving performance.
