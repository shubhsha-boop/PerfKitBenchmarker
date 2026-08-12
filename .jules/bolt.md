## 2024-08-12 - Avoid setdefault in hot loops
**Learning:** Using `dict.setdefault(key, default_obj)` inside a loop causes unnecessary memory allocation on every iteration because the default argument is evaluated eagerly.
**Action:** Replace `.setdefault` with `collections.defaultdict` for accumulating data in hot loops to lazily evaluate the default and improve performance.
