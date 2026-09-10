## 2026-09-10 - [Performance] dict.setdefault in hot loops
**Learning:** Using dict.setdefault(key, set()) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocation overhead.
**Action:** Replace it with collections.defaultdict(set) to lazily initialize the default value and improve performance.
