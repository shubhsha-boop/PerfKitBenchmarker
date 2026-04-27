## 2025-02-20 - [Avoid dict.setdefault with new objects in hot loops]
**Learning:** Using `dict.setdefault(key, default_obj)` (e.g., `set()`, `[]`, `{}`) inside a hot loop evaluates the default argument on every iteration, leading to unnecessary memory allocations and garbage collection overhead. This is a common performance anti-pattern.
**Action:** Replace `dict.setdefault(key, default_obj)` with `collections.defaultdict(default_type)` for cleaner and more performant code, as it lazily initializes the default value.
