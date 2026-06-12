## 2024-05-24 - Python Performance Anti-Pattern: dict.setdefault inside loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`, `[]`, or `{}`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replacing it with `collections.defaultdict` is the preferred optimization as it lazily initializes the default value, improving performance without sacrificing readability.
