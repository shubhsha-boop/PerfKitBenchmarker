## 2024-05-18 - Replacing dict.setdefault with defaultdict in Hot Loops
**Learning:** Using `dict.setdefault(key, default_obj)` inside a loop evaluates the `default_obj` (like `set()` or `[]`) on every single iteration, even if the key already exists. This causes unnecessary memory allocations and hurts performance, especially in frequently executed code like `publisher._FindConstantMetadataKeys`.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` for operations within loops to lazily initialize the default value and improve performance.
