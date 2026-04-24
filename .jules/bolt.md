## 2024-05-24 - Python Performance Anti-Pattern: dict.setdefault inside hot loops
**Learning:** Using `dict.setdefault(key, [])` inside a loop evaluating default values like empty lists or sets will still evaluate the default argument on every iteration, leading to memory allocations for every element. This pattern is common in the codebase, such as `kubernetes_events.py` and `aerospike_client.py`.
**Action:** Use `collections.defaultdict(list)` instead when aggregating values by key, as it lazily initializes the default value, improving performance without sacrificing readability.
