## 2024-05-24 - Avoid dict.setdefault inside loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace with `collections.defaultdict` which lazily initializes the default value, improving performance without sacrificing readability.
