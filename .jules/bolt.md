
## 2025-02-23 - Defaultdict Optimization in Hot Loops
**Learning:** Using `dict.setdefault(key, default_factory())` inside hot loops evaluates the `default_factory()` (e.g., `set()`, `[]`) on every iteration, leading to unnecessary object creation and memory allocation overhead. Replacing it with `collections.defaultdict` provides a measurable performance improvement (16-21% in microbenchmarks) without sacrificing readability.
**Action:** Always prefer `collections.defaultdict` over `dict.setdefault` when populating dictionaries with collections inside loops, especially when processing large datasets like performance samples.
