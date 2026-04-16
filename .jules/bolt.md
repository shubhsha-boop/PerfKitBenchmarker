## 2026-04-16 - [Replace setdefault anti-pattern]
**Learning:** Using dict.setdefault(key, []) or setdefault(key, set()) evaluates the default argument on every iteration, causing unnecessary memory allocations.
**Action:** Replaced dict.setdefault() with conditional object creations or collections.defaultdict() to speed up and reduce memory footprint.
