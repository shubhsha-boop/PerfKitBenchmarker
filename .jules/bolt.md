## 2025-05-14 - Pre-compile regexes in parsing loops
**Learning:** Evaluating `re.match` with string patterns inside frequently called parsing functions or loops introduces measurable overhead due to internal cache lookups or recompilation.
**Action:** Pre-compile regexes as module-level constants (`re.compile`) when they are used within loops or line-by-line parsing utilities to improve execution speed.
