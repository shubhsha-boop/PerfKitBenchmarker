## 2026-09-17 - Optimizing Dictionary Updates Inside Loops

**Learning:** When adding to dictionary sets within loops, using `setdefault(k, set())` forces Python to allocate a new empty `set()` on *every* iteration, which introduces measurable overhead. Using `collections.defaultdict(set)` avoids these continuous empty object allocations, resulting in significant performance gains for dict-heavy workloads like processing thousands of telemetry samples.

**Action:** Replace `setdefault(key, default_obj)` with `collections.defaultdict` when used inside high-frequency loops, but strictly ensure that benchmarking proves its impact on the real application.
