## 2025-05-07 - Python Performance Anti-Pattern: dict.setdefault in loops
**Learning:** Using `dict.setdefault(key, default_factory())` inside a loop evaluates the default argument on every iteration, which can cause unnecessary memory allocations and garbage collection overhead, especially when the default factory is `set()` or `[]`.
**Action:** Replace `dict.setdefault` inside hot loops with `collections.defaultdict`. This lazily initializes the default value, improving performance without sacrificing readability.
