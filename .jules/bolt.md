## 2024-05-24 - Avoid setdefault with instantiations inside loops
**Learning:** Using `dict.setdefault(key, default_obj)` (where `default_obj` is something like `[]` or `set()`) inside a loop evaluates `default_obj` on every iteration, causing unnecessary memory allocations.
**Action:** Use `collections.defaultdict` inside hot loops, as it evaluates the default factory lazily, improving performance.
