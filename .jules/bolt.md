## 2024-05-24 - setdefault inside loops
**Learning:** Using `dict.setdefault(key, set())` inside a tight loop evaluates the `set()` allocation on every iteration, leading to significant unnecessary overhead. Replacing it with `collections.defaultdict(set)` is substantially faster, up to 40-50% in benchmarks.
**Action:** When gathering items in collections within hot loops, use `collections.defaultdict` instead of `dict.setdefault`.
