## 2024-05-18 - Pre-compiled Regular Expressions
**Learning:** Python functions called inside loops or handling substantial output frequently compile their regular expressions on every invocation, causing unnecessary overhead.
**Action:** Always extract `re.compile()` calls out of function bodies to the module level as global constants for any regex used in hot paths or parsers.
