## 2024-05-18 - Python dict.setdefault() performance overhead
**Learning:** Using `dict.setdefault(key, set())` evaluates the default argument `set()` on every loop iteration, even if the key exists. In hot loops, this causes unnecessary object creation and garbage collection, resulting in a measurable performance overhead.
**Action:** Replace `dict.setdefault()` inside loops with `dict.get()` and a conditional check, or use `collections.defaultdict` when appropriate, to avoid unnecessary object instantiation.
