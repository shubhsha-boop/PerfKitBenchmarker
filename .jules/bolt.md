## 2025-02-28 - Using `dict.setdefault` in Hot Loops
**Learning:** `dict.setdefault(key, default_val)` evaluates `default_val` on every invocation regardless of key existence. Using it inside hot loops with mutable defaults like `set()` or `[]` incurs unnecessary memory allocation overhead.
**Action:** Use `collections.defaultdict` to defer default value instantiation until missing keys are actually accessed, which provides significant speedups in aggregation functions (like `publisher._FindConstantMetadataKeys`).
