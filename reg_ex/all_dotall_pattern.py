import re
all_pattern= re.compile(r'.*')

print(all_pattern.match('AI with Python.\n ML with Python.'))

all_with_next_pattern = re.compile(r'.*', re.DOTALL)

print(all_with_next_pattern.match('AI with Python.\nML with Python.\teverything with python.').group())