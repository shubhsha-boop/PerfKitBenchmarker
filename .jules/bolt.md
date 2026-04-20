## 2025-04-20 - [Performance Anti-Pattern: dict.setdefault(key, set())]
**Learning:** Using `dict.setdefault(key, set())` inside loops evaluates `set()` on every iteration, leading to unnecessary memory allocations and degraded performance.
**Action:** Replace `dict.setdefault(key, set())` with `dict.get(key)` and only instantiate the default object if the key does not exist.
