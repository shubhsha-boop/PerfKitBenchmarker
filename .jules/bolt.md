## 2024-06-01 - Python Performance Anti-Pattern: dict.setdefault with mutable defaults
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`, `[]`, or `{}`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with `collections.defaultdict` as the preferred optimization as it lazily initializes the default value, improving performance without sacrificing readability.
