## 2024-05-15 - [Avoid dict.setdefault in hot loops]
**Learning:** Python dictionary `setdefault(key, default_obj)` method eagerly evaluates `default_obj` on every execution. Inside a hot loop, passing things like `set()` creates a new empty set on every iteration which causes huge memory allocation overhead.
**Action:** Replace `dict.setdefault(key, default_obj)` with `collections.defaultdict(default_type)` for better performance while preserving readability.
