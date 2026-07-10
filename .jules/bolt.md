## 2024-07-10 - Python defaultdict Optimization
**Learning:** Using dict.setdefault(key, set()) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations and degrading performance.
**Action:** Use collections.defaultdict(set) instead for lazy initialization of default values.
