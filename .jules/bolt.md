## 2026-08-27 - Prevent Unnecessary Object Allocation in Loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()` or `[]`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with `collections.defaultdict` when initializing mutable defaults to lazily initialize the default value, improving performance.
