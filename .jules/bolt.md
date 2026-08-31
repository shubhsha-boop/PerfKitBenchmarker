## 2024-05-18 - Replacing dict.setdefault with collections.defaultdict in hot loops
**Learning:** Using dict.setdefault(key, set()) evaluates the default argument on every iteration inside a loop, causing unnecessary allocations.
**Action:** Replace dict.setdefault with collections.defaultdict to improve performance.
