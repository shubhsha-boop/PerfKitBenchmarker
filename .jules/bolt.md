## 2026-09-07 - Optimize hot loops by avoiding dict.setdefault
**Learning:** Using dict.setdefault(key, set()) inside a loop evaluates the default argument (set()) on every iteration, leading to unnecessary memory allocations and performance degradation, particularly in hot paths like sample metadata processing.
**Action:** Replace dict.setdefault with collections.defaultdict in hot loops to lazily initialize default values, improving performance without sacrificing readability.
