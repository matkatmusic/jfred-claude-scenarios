"""Rename one/two/three.py to core_one/core_two/core_three.py."""
import shutil

for name in ("one", "two", "three"):
    shutil.move(f"{name}.py", f"core_{name}.py")
    print(f"{name}.py -> core_{name}.py")
