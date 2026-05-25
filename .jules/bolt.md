## 2024-05-21 - [dict.setdefault vs collections.defaultdict in python loops]
**Learning:** [Using `dict.setdefault(key, default_obj)` inside a hot loop evaluates the `default_obj` (like `set()`) on every iteration, causing unnecessary memory allocations. This is particularly impactful in Python loops processing metadata or aggregates.]
**Action:** [Use `collections.defaultdict` instead of `dict.setdefault` when dynamically building nested structures like dictionary of sets or lists in performance-critical sections to ensure the default factory is lazily evaluated.]
