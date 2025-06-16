import re
optional_pattern = re.compile(r'42!')

print(optional_pattern.search('42'))
print(optional_pattern.search('42!'))
print(optional_pattern.search('42$'))
print(optional_pattern.search('42$'))



optional_pattern= re.compile(r'(\d{2})?!')
print(optional_pattern.search('42!'))
print(optional_pattern.search('!'))
print(optional_pattern.search('42'))