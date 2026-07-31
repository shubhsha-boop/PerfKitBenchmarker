## 2025-05-18 - Avoid unnecessary memory allocations in loops with dict.setdefault
**Learning:** Python's `dict.setdefault(key, default_val)` eagerly evaluates the default argument on every iteration. When the default is a mutable object like `set()` or `[]` and used in a tight loop, it causes redundant memory allocations for default objects that often go unused.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` inside hot loops to lazily initialize the default value, improving performance and memory efficiency without sacrificing readability.
