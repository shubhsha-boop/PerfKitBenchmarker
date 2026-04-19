
## 2024-05-18 - Replacing dict.setdefault with dict.get in Loops
**Learning:** In Perfkitbenchmarker, there are multiple loops (e.g., in publisher.py, kubernetes_events.py, aerospike_client.py) iterating over large numbers of samples or events. Using `dict.setdefault(k, set())` inside these hot loops evaluates the default `set()` (or `[]`) on every iteration, causing unnecessary memory allocation and overhead.
**Action:** Replace `dict.setdefault()` with `.get()` and conditionally instantiate the default object when the key is missing inside loops processing large inputs to reduce unnecessary memory allocation.
