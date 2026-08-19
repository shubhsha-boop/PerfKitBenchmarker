## 2024-05-24 - DefaultDict Optimization
**Learning:** Using `dict.setdefault()` inside loops creates the default object (like an empty list `[]`) on every iteration, leading to unnecessary memory allocations and slight performance degradation, even if the key exists.
**Action:** Replace `dict.setdefault(key, []).append(val)` with `collections.defaultdict(list)` for better performance and cleaner code.
