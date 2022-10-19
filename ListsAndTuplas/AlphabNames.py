import operator

PEOPLE = [
    {'first':'Jorge', 'last':'Lerner'},
    {'first':'Maria', 'last':'Gonzalez' },
    {'first':'Peter', 'last':'Smith' }
]

def alphabetize_names(list_of_dicts):
# The “key” parameter
# to “sorted” gets a
# function, whose result
# indicates how we’ll sort.
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first')) #key is afunction que recive como parametro list_of_dicts

print(alphabetize_names(PEOPLE))
# print(operator.itemgetter('last', 'first'))





#How itemgetter works:

s = 'abcdef'
t = (10, 20, 30, 40, 50, 60)
get_2_and_4 = operator.itemgetter(2, 4)
print(get_2_and_4(s))
print(get_2_and_4(t))


