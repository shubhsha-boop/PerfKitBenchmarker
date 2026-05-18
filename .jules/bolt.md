
## 2025-02-20 - Python Dictionary Hot Loop Allocation
**Learning:** Found an instance in `perfkitbenchmarker/publisher.py` where `dict.setdefault(k, set())` was used inside a high-frequency nested loop. Because Python eagerly evaluates function arguments, a new empty `set()` is allocated in memory and immediately discarded on every iteration where the key already exists.
**Action:** Always replace `dict.setdefault(key, default_factory())` with `collections.defaultdict(default_factory)` in performance-sensitive hot loops to avoid redundant memory allocations and unnecessary garbage collection overhead.
