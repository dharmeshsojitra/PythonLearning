import re

match_with_dot_pattern = re.compile(r'.at')
print(match_with_dot_pattern.findall('the cat in the hat sat on the flat mat.'))