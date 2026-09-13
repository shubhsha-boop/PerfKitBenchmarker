## 2026-09-13 - Avoid dict.setdefault in hot loops
**Learning:** Using dict.setdefault(key, default_obj) (like set() or []) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with collections.defaultdict as it lazily initializes the default value, improving performance without sacrificing readability.
