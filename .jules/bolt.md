## 2026-09-18 - Optimize dict.setdefault in Publisher
**Learning:** Using dict.setdefault(key, set()) in tight loops evaluates the default argument (e.g., allocating an empty set) on every iteration, creating unnecessary memory overhead and GC pressure.
**Action:** Replace dict.setdefault with collections.defaultdict in high-frequency operations when appropriate to improve execution time.
