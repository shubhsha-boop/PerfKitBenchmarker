## 2024-05-18 - Avoid dict.setdefault in hot loops
**Learning:** Using `dict.setdefault(key, set())` inside a hot loop (like iterating through sample metadata in `publisher.py`) evaluates the default argument (`set()`) on every iteration, causing unnecessary memory allocations.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` to lazily initialize the default value and prevent redundant object allocations without sacrificing readability.
