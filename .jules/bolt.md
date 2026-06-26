## 2024-06-26 - [Python Performance Anti-Pattern]
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`) inside a loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replacing it with `collections.defaultdict` is the preferred optimization as it lazily initializes the default value, improving performance without sacrificing readability.
