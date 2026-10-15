## 2026-10-15 - Optimize hot serialization paths
**Learning:** In hot serialization paths (like sample metadata processing), using `dict.setdefault()` evaluates the default argument on every iteration, causing unnecessary overhead. Replacing it with `collections.defaultdict` provides a measurable speedup without sacrificing readability.
**Action:** Prefer `collections.defaultdict` over `dict.setdefault` in loops within hot paths to avoid empty object allocation overhead.
