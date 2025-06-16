import re

zero_or_more_pattern = re.compile(r'AI (with Py)*(thon|charm)?')

print(zero_or_more_pattern.search('AI with Python'))
print(zero_or_more_pattern.findall('AI with Python, AI with Pycharm or Java'))