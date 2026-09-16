## 2026-09-16 - Pre-compile regex for performance
**Learning:** Compiling regex patterns (e.g. `re.compile()`) inside loops causes significant overhead as they are re-evaluated each iteration.
**Action:** Extract `re.compile()` outside of loops to pre-compile the patterns for measurable performance gains in parsing intensive utilities.
## 2026-09-16 - defaultdict optimization for inner loop memory and performance
**Learning:** Using `dict.setdefault()` inside a loop evaluates the default argument on every iteration which causes unnecessary allocations. Replacing it with `collections.defaultdict` provides measurable performance improvements for loops aggregating values.
**Action:** When aggregating or grouping values in a tight loop, avoid `dict.setdefault(key, default_obj)` and use `collections.defaultdict(default_type)` instead to avoid redundant evaluations and allocations.
