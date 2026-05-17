## 2026-05-17 - Dict Setdefault Inside Loops
**Learning:** Using `dict.setdefault(key, default_obj)` (like `[]` or `set()`) inside a high-frequency loop is a common Python performance anti-pattern because the default argument is initialized on every single iteration, even if the key already exists. This wastes CPU cycles and memory.
**Action:** Always replace `dict.setdefault()` with `collections.defaultdict` when initializing dictionaries that will be populated inside a loop, as it lazily evaluates the default object.
