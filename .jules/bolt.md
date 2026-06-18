## 2024-05-24 - Optimization: defaultdict vs setdefault in hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`) inside a loop evaluates `default_obj` on every iteration, causing unnecessary memory allocations.
**Action:** Replace `setdefault` with `collections.defaultdict` to lazily initialize the default value, improving performance without sacrificing readability.
