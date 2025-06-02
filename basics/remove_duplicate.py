numbers = [99,3,34,3]
print(f'list is {numbers}')
for number in numbers:
    if numbers.count(number)> 2 :
        numbers.remove(number)
print(f'list after removing duplicate is {numbers}')


print(f'the last element in the list is {numbers[-1]}')

print(f'the second last element in the list is {numbers[-3]}')

numbers[3] = 23
print(f'the list is {numbers} after adding 23 to it')

numbers.sort()
print(f'the list is {numbers} after sorting it in place')


at_index = numbers.index(1)
print(f'the last element in the list is {at_index}')