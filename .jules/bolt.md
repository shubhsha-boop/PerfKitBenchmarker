## 2026-08-28 - [Replace dict.setdefault with collections.defaultdict in hot loops]
**Learning:** [Using dict.setdefault(key, set()) inside a hot loop evaluates the default argument (set()) on every iteration, causing unnecessary memory allocations. Replacing it with collections.defaultdict lazily initializes the default value, improving performance by avoiding redundant object creation.]
**Action:** [Identify and replace dict.setdefault with collections.defaultdict in high-frequency loops or data aggregation functions.]
