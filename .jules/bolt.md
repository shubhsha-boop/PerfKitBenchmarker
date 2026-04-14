## 2026-04-14 - Regular expression compilation
**Learning:** Compiling regular expressions repeatedly inside loops or functions can cause performance overhead. Move `re.compile()` to the module level.
**Action:** When finding `re.compile()` used locally, move it to module-level constants for better performance.
