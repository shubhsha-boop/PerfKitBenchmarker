## 2026-08-25 - [Optimize dict.setdefault in hot loop]
**Learning:** Using dict.setdefault(key, default_obj) inside a hot loop (like setdefault(k, set())) evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace dict.setdefault with collections.defaultdict to lazily initialize default values for better performance.
