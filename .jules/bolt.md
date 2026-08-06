## 2024-08-06 - Replacing dict.setdefault with collections.defaultdict in Hot Loops
**Learning:** Using dict.setdefault(key, default_obj) inside a loop evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Use collections.defaultdict in hot loops instead of dict.setdefault when dealing with mutable defaults like lists or sets.
