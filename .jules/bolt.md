
## 2025-06-05 - Temporary Benchmarking Scripts Pollution
**Learning:** Adding test or benchmarking scripts to the repository root for measurement purposes pollutes the environment. Code review will flag these if they are accidentally left behind.
**Action:** Always delete temporary benchmark scripts using `rm <filename>` immediately after extracting the measurement results and before creating a pull request or submitting code.
