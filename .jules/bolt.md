## 2024-05-18 - Avoid committing scratch files
**Learning:** Temporary micro-benchmark scripts (like `test_setdefault*.py`) created to measure performance must be deleted before submission to avoid polluting the repository.
**Action:** Always run `rm` on any temporary scripts or output files created during the verification phase before finalizing the PR.
