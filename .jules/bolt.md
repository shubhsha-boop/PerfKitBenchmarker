## 2024-08-25 - Replace setdefault with defaultdict in hot loops
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop in Python unnecessarily allocates a new `set` object on every iteration, which degrades performance and memory efficiency.
**Action:** Use `collections.defaultdict(set)` (or `list`, etc.) when appending to collections in a loop to lazily initialize default values without the allocation overhead.
