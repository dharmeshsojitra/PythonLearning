import re
piped_regex = re.compile(r'ju(ice|mp|g|st)')

def get_from_piped_regex(text):
    match = piped_regex.search(text)
    if match:
        return match.group()
    else:
        return None

print(get_from_piped_regex('just chill out chill out just chill out'))
print(get_from_piped_regex('jaa jaa j j ja ju ju j j j '))