
## 2025-02-28 - Avoid dict.setdefault() with default object creation in hot loops
**Learning:** Using `dict.setdefault(key, [])` or `dict.setdefault(key, set())` inside a hot loop is a performance anti-pattern. Even if the key exists, Python evaluates the default argument on every single iteration, causing unnecessary memory allocations and garbage collection overhead.
**Action:** Always replace `dict.setdefault(key, default_obj)` in loops with `collections.defaultdict` when aggregating data, as it lazily initializes the default value.
