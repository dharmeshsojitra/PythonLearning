import re

no_finding_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
grp_phone_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
txt = "I can find any hidden876-090-6666n umber correctly"

def fing_number_from_text(text):
    phone_number = no_finding_regex.search(text)
    return phone_number.group()

def find_grp_in_number(text,grp_no):
    grps = grp_phone_regex.search(text)
    grps = grps.group(grp_no)
    return grps

print(fing_number_from_text(txt))

grp = find_grp_in_number(txt,1)
print(f'first group of the text: {txt} is {grp}')

grp = find_grp_in_number(txt,2)
print(f'Second group of the text:{txt} is {grp}')

grp = find_grp_in_number(txt,3)
print(f'Third group of the text:{txt} is {grp}')

grp = find_grp_in_number(txt,0)
print(f'the whole group of the text:{txt} is {grp}')