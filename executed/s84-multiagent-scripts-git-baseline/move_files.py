import shutil

src, dst = "inventory.py", "core_inventory.py"
shutil.move(src, dst)
print(f"Renamed: {src} -> {dst}")
