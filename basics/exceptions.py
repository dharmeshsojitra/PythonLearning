def divide_num(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 'division by zero not allowed'

print(divide_num(5, 2))
print(divide_num(5, 0))





