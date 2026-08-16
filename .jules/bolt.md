## 2024-08-16 - dict.setdefault Performance Anti-Pattern
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()` or `[]`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations even if the key exists. In our micro-benchmarks, this added significant overhead.
**Action:** Replace `dict.setdefault` with `collections.defaultdict(type)` in performance-sensitive loops, as it lazily initializes the default value, improving performance without sacrificing readability.
