## 2024-05-24 - Avoid `dict.setdefault()` inside loops
**Learning:** Using `dict.setdefault(key, set())` inside a loop in Python evaluates the second argument (e.g., creating a new empty `set`) on every iteration, leading to unnecessary memory allocation and CPU overhead if the key already exists.
**Action:** Replace `dict.setdefault()` with `collections.defaultdict(set)` when initializing values inside hot loops to defer evaluation and improve performance without changing behavior.
