## 2024-06-25 - Performance Anti-Pattern: dict.setdefault inside loops
**Learning:** Using `dict.setdefault(key, default_obj)` (e.g. with `set()`, `[]`, or `{}`) inside a hot loop evaluates the default argument on every iteration, leading to unnecessary memory allocations and degraded performance.
**Action:** Replace `dict.setdefault` inside high-frequency loops with `collections.defaultdict` which lazily initializes the default value, improving speed without sacrificing readability.
