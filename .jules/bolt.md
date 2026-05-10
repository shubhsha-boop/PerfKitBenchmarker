## 2025-05-10 - Python dict.setdefault Anti-pattern in loops
**Learning:** Using `dict.setdefault(key, default_obj)` inside a hot loop in Python is a performance anti-pattern because the default argument (like `set()` or `[]`) is evaluated on every iteration, causing unnecessary memory allocations even if the key already exists.
**Action:** Replace `dict.setdefault` in loops with `collections.defaultdict` for better performance and lazy initialization, especially for high-frequency or inner-loop operations.
