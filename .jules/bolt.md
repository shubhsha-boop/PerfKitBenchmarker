## 2026-09-12 - Avoid dict.setdefault with mutable defaults in loops
**Learning:** Using dict.setdefault(key, set()) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with collections.defaultdict(set) to lazily initialize the default value and avoid repeated allocations, improving performance without sacrificing readability.
