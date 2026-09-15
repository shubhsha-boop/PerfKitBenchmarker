## 2026-09-15 - Use collections.defaultdict for efficient dict population
**Learning:** Using `dict.setdefault(key, set())` inside loops evaluates the default argument (`set()`) on every iteration, causing unnecessary memory allocations. `collections.defaultdict` lazily initializes the default value.
**Action:** Replace `dict.setdefault(key, default_obj)` with `collections.defaultdict(type)` in hot loops.
