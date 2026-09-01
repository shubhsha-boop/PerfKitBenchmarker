## 2026-09-01 - Python dict.setdefault anti-pattern in hot loops
**Learning:** Using dict.setdefault(key, set()) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with collections.defaultdict(set) to lazily initialize default values, improving performance without sacrificing readability.
