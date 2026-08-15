## 2024-08-15 - Python Performance Anti-Pattern: dict.setdefault inside loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations. This is an anti-pattern when optimizing for performance.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` to lazily initialize the default value, improving performance without sacrificing readability.
