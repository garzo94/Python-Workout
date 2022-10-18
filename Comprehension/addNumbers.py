def sum_numbers(numbers):
    return sum(int(number)
               for number in numbers.split()
               if number.isdigit())

print('1 x 0 .3 56 k4 5'.split())
