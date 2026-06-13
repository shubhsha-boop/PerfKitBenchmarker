## 2024-05-18 - Avoid setdefault with expensive defaults in loops
**Learning:** Using `dict.setdefault(k, set())` inside a hot loop in Python is an anti-pattern. The default argument (`set()`) is evaluated on every iteration, causing unnecessary memory allocations even when the key already exists.
**Action:** Replace `dict.setdefault(k, set())` with `collections.defaultdict(set)`. This lazily initializes the default value only when the key is missing, providing a measurable performance improvement without sacrificing readability.
