import re
vowel_pattern = re.compile(r'[aeiouAEIOU]')

no_vowel_pattern = re.compile(r'[^aeiouAEIOU]')

def get_vowel(text):
    return vowel_pattern.findall(text)

def get_no_vowel(text):
    return no_vowel_pattern.findall(text)

print(get_vowel('I am a boy'))

print(get_no_vowel('I am a boy'))