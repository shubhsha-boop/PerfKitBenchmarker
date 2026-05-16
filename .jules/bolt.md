## 2025-05-16 - dict.setdefault in Hot Loops
**Learning:** `dict.setdefault(k, default_value)` evaluates `default_value` on *every* loop iteration before checking the dict. In high-frequency parsing paths (like Publisher sample aggregation), passing expressions like `set()` or `[]` to `setdefault` creates significant hidden allocation/GC overhead.
**Action:** Replace `dict.setdefault` with `collections.defaultdict` for accumulating collections during aggregation loops.
