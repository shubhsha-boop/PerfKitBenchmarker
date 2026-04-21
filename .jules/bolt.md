## 2024-05-14 - Python Performance Anti-Pattern: dict.setdefault with mutable objects
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop (like `perfkitbenchmarker/publisher.py` metadata aggregation) evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replace it with `collections.defaultdict(set)` or `collections.defaultdict(list)` which lazily initialize the default value to provide a measurable speedup without sacrificing readability.
