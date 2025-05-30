for i in range(1,6):
    if i == 1 or i ==3:
        print('X' * 5)
    else:
        print('X' * 2)


#sol 2
numbers= [5, 2,5,2,2]
for number in numbers:
    no_of_x = number
    design = ''
    for x in range(no_of_x):
        design = design + 'X'
    print(design)


