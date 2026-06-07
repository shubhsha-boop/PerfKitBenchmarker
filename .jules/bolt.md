## 2024-05-24 - Avoid dict.setdefault with mutable defaults in loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`, `[]`, or `{}`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with `collections.defaultdict` to lazily initialize the default value, improving performance without sacrificing readability.
