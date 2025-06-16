import re

pattern = re.compile(r'\d{3}')

def find_all_matches(text):
    return pattern.findall(text)

print(find_all_matches('My344 name is 767 Alex777'))