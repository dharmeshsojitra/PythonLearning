import re

no_finding_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

def fing_number_from_text(text):
    phone_number = no_finding_regex.search(text)
    return phone_number.group()


print(fing_number_from_text("I can find any hidden876-090-6666n umber correctly"))
