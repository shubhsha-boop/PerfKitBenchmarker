## 2025-05-28 - Avoid setdefault in hot loops
**Learning:** Using dict.setdefault(key, set()) inside tight loops evaluates the default argument on every iteration, leading to unnecessary memory allocations.
**Action:** Use collections.defaultdict(set) for lazy initialization and improved performance.
