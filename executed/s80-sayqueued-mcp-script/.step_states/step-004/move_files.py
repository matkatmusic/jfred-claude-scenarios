"""Rename one/two/three.py to core_one/core_two/core_three.py."""
import shutil

for n in ("one", "two", "three"):
    old, new = f"{n}.py", f"core_{n}.py"
    shutil.move(old, new)
    print(f"{old} -> {new}")
