
from pathlib import Path
import os


def all_files(dir, pattern):
    """Recursively finds every file in 'dir' whose name matches 'pattern'."""
    return [f.as_posix() for f in [x for x in Path(dir).rglob(pattern)]]


if __name__ == "__main__":
    svgs = all_files('.', '*.svg')

    command = 'inkscape -g --batch-process --verb="EditSelectAll;StrokeToPath;FileSave;FileClose;" '

    os.system(command + ' '.join(svgs[600:1000]))
