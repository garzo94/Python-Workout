# when you retrieve a slice from an object x, you get back a new
# object of the same type as x. But if you retrieve an individual element from x, you’ll get
# whatever was stored in x—which might be the same type as x, but you can’t be sure


# my solution:
seq = ('a', 'b', 'c', 'd')

def firstlat(sequence):
    return sequence[:1] + sequence[-1:]

print(firstlat('abc'))

#book solution
def firstlast(sequence):
    return sequence[:1] + sequence[-1:]
print(firstlast('abcd'))

# iterate over just the final n elements of a list.
# mylist[-3:]
