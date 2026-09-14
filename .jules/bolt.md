## 2026-09-14 - Replace dict.setdefault() with collections.defaultdict() inside loops
**Learning:** Using `dict.setdefault(key, [])` inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations. It is significantly slower than using `collections.defaultdict`.
**Action:** Replace `dict.setdefault(key, [])` with `collections.defaultdict(list)` in loops to lazily initialize default values, improving performance without sacrificing readability.
