from os import path
from pathlib import Path
from zipfile import ZipFile
import shutil

#source = Path("ecommerce/__init__.py")
#target = Path() / "__init__.py"
#shutil.copy(source, target)
#target.write_text(source.read_text())

with ZipFile("files.zip", "w") as zip:
    for path in Path in Path("ecommerce").rglob("*.*"):
        zip.write(path)