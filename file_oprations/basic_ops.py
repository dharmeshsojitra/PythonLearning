from pathlib import Path
import os
print(Path('spam') / 'bacon' / 'eggs')

print(
    Path('spam') / 'bacon' / 'eggs'
)

print(
    Path('spam') / Path('bacon', 'eggs')
)

print(
    'spam' / Path('bacon', 'eggs')
)

print(
    Path.cwd()
)

print(os.getcwd())


print (Path.home())