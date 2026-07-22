"""Rename one/two/three.py to core_one/core_two/core_three.py."""
import shutil

shutil.move("one.py", "core_one.py")
shutil.move("two.py", "core_two.py")
shutil.move("three.py", "core_three.py")
print("Done.")
