## 2024-05-15 - dict.setdefault Performance Anti-pattern
**Learning:** Using dict.setdefault(key, set()) inside a hot loop evaluates the default argument on every iteration, causing unnecessary memory allocations and degrading performance.
**Action:** Replace dict.setdefault with collections.defaultdict to lazily initialize default values, improving performance without sacrificing readability.
