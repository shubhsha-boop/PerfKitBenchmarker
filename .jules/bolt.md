## 2024-05-18 - Dictionary setdefault in nested loops
**Learning:** Using `dict.setdefault(key, set())` inside nested loops evaluates the default argument (`set()`) on every iteration, leading to unnecessary memory allocations and CPU overhead, especially when iterating over many samples and metadata keys.
**Action:** Replace `setdefault` with `collections.defaultdict` for accumulating data in dictionaries within hot loops to lazily initialize default values, improving performance by avoiding redundant instantiations.
