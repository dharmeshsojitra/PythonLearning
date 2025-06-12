import re

reg_ex = re.compile(r'\(\d{3}\)')

def match_pattern(text):
    match = reg_ex.search(text)
    try:
        return match.group()
    except AttributeError:
        return 'match not found'

print(match_pattern('hello (123) '))