## 2024-05-24 - Avoid default evaluations in Python loops
**Learning:** `dict.setdefault(k, default_val)` evaluates `default_val` before the function call, which in hot loops means unnecessary allocations even if the key exists (e.g. `set()` creates an empty set object).
**Action:** When initializing missing keys to a mutable default type like `set`, `list`, or `dict`, use `collections.defaultdict` to prevent evaluating the default on every iteration.
