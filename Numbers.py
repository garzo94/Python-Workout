# import random
#
#
# def guessing_game():
#     random_integer = random.randint(1, 100)
#     return random_integer
#
# guessing_number = guessing_game()
# name = input('Enter your name: ')
#
# if name is None:
#     name = ''
# print(f'Hello {name}')
# number = int(input('guess a number'))
#
#
# while number != guessing_number:
#     if number > guessing_number:
#         print('Too high')
#         number=int(input('try again'))
#     elif number < guessing_number:
#         print('Too low')
#         number = int(input('try again'))
#     elif number == guessing_number:
#         brea


####  Exercise2  ######

# def mysum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# var = mysum(*[1,5,3]) or
# var = mysum(1,5,3)
# print(var) == 9

####  Exercise-3  ######

# def run_time():
#     time = input('Enter 10 km run time:  ') #empty string is considered false
#     return time
# averageList =[]
# mysum = 0
# while True:
#     mytime = run_time()
#     try:
#         if mytime:
#             averageList.append(float(mytime))
#     except ValueError as e:
#         print('Thats not a valid number')
#     if not mytime:
#         for time in averageList:
#             mysum += time
#         average = mysum / len(averageList)
#         print(average)
#
#         break

### Exercise -4 ##

# def hex_output():
#     sum_values = []
#     while True:
#         hex_number = input('enter a hex number: ')
#         letters_value = {
#             'a': 10,
#             'b': 11,
#             'c': 12,
#             'd': 13,
#             'e': 14,
#             'f': 15,
#         }
#         if not hex_number:
#             break
#         else:
#             for index, value in enumerate(reversed(hex_number)):
#               try:
#                    val = (16**int(index))*int(value)
#                    sum_values.append(val)
#               except:
#                   val = (16 ** int(index)) * int(letters_value[value])
#                   sum_values.append(val)
#
#
#         total = 0
#
#         for val in sum_values:
#             total += int(val)
#         print(total)
#         sum_values.clear()
#
# hex_output()

#### String #####
## Excersise 5 ####






