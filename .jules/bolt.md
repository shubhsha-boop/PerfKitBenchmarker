## 2024-05-18 - Avoid committing local test scripts
**Learning:** Even when requested to be performance obsessed and write local benchmark scripts to measure impacts, these scratchpad scripts (like `test_perf.py`) must be deleted before finalizing the commit, as adding them clutters the source code repository.
**Action:** Always verify with `git status` or `ls` that only explicitly intended source files are modified or added before requesting review or submitting.
