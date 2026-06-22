## 2024-05-24 - Pre-compiling regex outside loops
**Learning:** In Python, repeatedly calling `re.compile()` inside a high-frequency loop or function causes unnecessary overhead, as the pattern is re-evaluated each time, preventing maximum efficiency.
**Action:** Always extract `re.compile()` calls for constant patterns outside loops and, preferably, pre-compile them at the module level.
