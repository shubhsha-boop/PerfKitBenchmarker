## 2026-08-29 - Optimize Python dictionary initialization
**Learning:** Using `dict.setdefault(key, [])` inside a hot loop evaluates the default argument `[]` on every iteration, causing unnecessary memory allocations.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` to lazily initialize the default value, improving performance without sacrificing readability.
