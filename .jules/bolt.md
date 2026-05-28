## 2026-05-28 - Optimize setdefault in hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` inside a hot loop evaluates the default argument (e.g., `set()`) on every iteration, causing unnecessary memory allocations. This is a common performance anti-pattern.
**Action:** Replace `setdefault` inside loops with `collections.defaultdict` when the default object requires initialization, as it lazily initializes the value only when the key is missing.
