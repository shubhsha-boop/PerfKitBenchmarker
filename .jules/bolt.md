## 2026-09-28 - [Optimize _FindConstantMetadataKeys performance]
**Learning:** Using dict.setdefault(key, set()) inside a hot loop causes empty sets to be instantiated on every iteration, leading to significant overhead. This function processes metadata for every published sample, causing it to be heavily trafficked. Replacing setdefault with collections.defaultdict(set) removes this overhead.
**Action:** Use collections.defaultdict(set) instead of dict.setdefault(key, set()) in loops to avoid unnecessary object creations and overhead.
