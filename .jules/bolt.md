## 2026-10-01 - Avoid dict.setdefault inside loops for objects
**Learning:** Using dict.setdefault(key, default_obj) inside a loop evaluates the default argument on every iteration. This can cause redundant empty object allocations (like set()) in hot loops, causing unnecessary overhead.
**Action:** Replace dict.setdefault with collections.defaultdict when aggregating data inside loops if the default object requires initialization overhead, verifying the impact beforehand.
