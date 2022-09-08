#mys olution
def ubbi_dubbi(word):
    output = ''
    for letter in word:
        if letter in 'aeiou':
            output += f'ub{letter}'
        else:
            output +=  letter
    print(output)


ubbi_dubbi('elephant')

# book solution
# def ubbi_dubbi(word):
#     output = []
#     for letter in word:
#         if letter in 'aeiou':
#             output.append(f'ub{letter}')
#         else:
#             output.append(letter)
#     return ''.join(output) <--- 'character to join every element in iterator'.join(iterator)
#
# print(ubbi_dubbi('python'))
