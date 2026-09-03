## 2026-09-03 - [Replace setdefault with defaultdict in hot loops]
**Learning:** Using `dict.setdefault(key, default_obj)` (like `set()`) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations and garbage collection pressure.
**Action:** Replace `setdefault` with `collections.defaultdict` to lazily initialize the default value, improving performance without sacrificing readability.
