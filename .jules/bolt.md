
## 2024-05-20 - Avoid setdefault in hot loops
**Learning:** Using `setdefault(key, set())` inside a tight loop evaluates the `set()` constructor on every single iteration, even when the key already exists. This causes unnecessary object creation and memory allocation.
**Action:** When working in hot paths, replace `setdefault(k, default_val())` with a check like `if k not in dict: dict[k] = default_val()` to delay instantiation until it's actually needed.
