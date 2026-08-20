## 2024-08-20 - Avoid dict.setdefault inside loops
**Learning:** Python Performance Anti-Pattern: Using `dict.setdefault(key, default_obj)` (like `set()`, `[]`, or `{}`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations. Replacing it with `collections.defaultdict` is the preferred optimization as it lazily initializes the default value, improving performance without sacrificing readability.
**Action:** When a default value needs to be instantiated, use `collections.defaultdict` instead of `dict.setdefault` inside high-frequency loops.
