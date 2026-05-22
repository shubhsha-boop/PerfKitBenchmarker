## 2024-05-24 - Avoid dict.setdefault in hot loops
**Learning:** dict.setdefault evaluates the default argument on every iteration, causing unnecessary memory allocations and garbage collection when used in hot loops.
**Action:** Replace dict.setdefault with collections.defaultdict in high-frequency iterations to lazily initialize default values, improving performance without sacrificing readability.
