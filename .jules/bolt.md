## 2024-05-24 - Avoid dict.setdefault inside loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`) inside a loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with `collections.defaultdict` to lazily initialize the default value, improving performance without sacrificing readability.
