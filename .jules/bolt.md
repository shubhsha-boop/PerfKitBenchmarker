## 2026-09-05 - Replace setdefault with defaultdict in hot loop
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop evaluates `set()` on every iteration, causing unnecessary memory allocations. `collections.defaultdict(set)` lazily initializes, improving performance and reducing memory overhead.
**Action:** Use `collections.defaultdict` instead of `dict.setdefault` when setting default objects (lists, sets, dicts) in loops.
