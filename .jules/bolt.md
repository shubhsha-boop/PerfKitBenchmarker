
## 2025-05-18 - Avoid setdefault in Hot Loops
**Learning:** In PerfKitBenchmarker's `publisher.py` (specifically `_FindConstantMetadataKeys`), the use of `dict.setdefault(k, set())` inside a hot loop iterating over sample metadata evaluated `set()` on every single iteration, even if the key already existed. This is a classic Python performance anti-pattern that causes unnecessary memory allocations and CPU overhead, especially when processing many samples with numerous metadata entries.
**Action:** Replace `dict.setdefault(key, default_type())` with `collections.defaultdict(default_type)` for hot loop aggregations to lazy-initialize default values and avoid redundant evaluations.
