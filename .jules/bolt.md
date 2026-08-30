## 2025-02-27 - Use defaultdict over setdefault in Python hot loops
**Learning:** Using dict.setdefault(key, set()) in a hot loop evaluates the default argument on every iteration, leading to unnecessary memory allocations and degraded performance.
**Action:** Replace dict.setdefault with collections.defaultdict in hot paths for lazy initialization of default values, improving execution speed and reducing memory pressure.
