## 2026-09-24 - [Optimize dictionary setdefault in loop]
**Learning:** Using `dict.setdefault(key, set())` inside a loop evaluating samples evaluates the default argument (the empty set) on every single iteration, which creates unnecessary empty object allocations in hot loops.
**Action:** Use `collections.defaultdict` when initializing dictionaries in loops to avoid redundant allocation of default objects, unless explicitly instructed otherwise or micro-optimizing an unproven cold path.
