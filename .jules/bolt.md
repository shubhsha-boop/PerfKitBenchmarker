## 2024-05-18 - Replacing dict.setdefault with collections.defaultdict
**Learning:** Python dict.setdefault() inside a loop evaluates its second argument on every iteration, which can cause unnecessary memory allocations if the default value is a complex object like a list or dictionary.
**Action:** Use `collections.defaultdict` when possible instead.
