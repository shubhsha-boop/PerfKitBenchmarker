## 2024-05-14 - Replace dict.setdefault with collections.defaultdict
**Learning:** Using `dict.setdefault(key, [])` or `dict.setdefault(key, set())` inside loops evaluates the default argument on every iteration, leading to unnecessary object creation and memory allocation.
**Action:** Replace `dict.setdefault` with `collections.defaultdict(list)` or `collections.defaultdict(set)` when constructing dictionaries in a loop.
