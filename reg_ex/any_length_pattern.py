import re

text = '283948 India1839 9298 0393 ***india'
any_length_pattern = re.compile(r'\d+')
print(any_length_pattern.findall(text))


any_length_word_pattern = re.compile(r'\w+')
print(any_length_word_pattern.findall(text))