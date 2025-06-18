from pathlib import Path


for name in Path.cwd().glob('*'):
    print(name)