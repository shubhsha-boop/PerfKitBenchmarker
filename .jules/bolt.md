## 2025-02-26 - Avoid dict.setdefault in hot loops
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop in Python is an anti-pattern because the default value (`set()`) is evaluated and allocated on every single iteration, even if the key exists.
**Action:** Use `collections.defaultdict(set)` instead to lazily initialize the default value, improving performance and reducing memory allocations.
