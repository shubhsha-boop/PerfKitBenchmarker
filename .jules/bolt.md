## 2026-07-29 - Python dict.setdefault in hot loops
**Learning:** Found that using `dict.setdefault(key, set())` inside a tight loop causes a new empty set to be instantiated on every single iteration before passing it to `setdefault`, leading to a measurable allocation bottleneck even when the key already exists.
**Action:** Replace `dict.setdefault(k, default_factory())` with `collections.defaultdict(default_factory)` in hot loops across the codebase for a cheap ~2x speedup in dictionary grouping logic.
