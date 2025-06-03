numbers = [100,200,3,5,63,20,500,99,3,34]
largest = numbers[0]

for number in numbers:
    if number  > largest:
        largest = number

print(f'largest numbers in the list {numbers} is {largest}')


rev_numbers = sorted(numbers, reverse=True)
print(f'largest number in the list {rev_numbers[0]}')
