def binary_search(list, item):
 low = 0
 high = len(list)-1
 counter=0
 while low <= high:
    mid = (low + high) # this is not the middle is the total of the array, I think is a mistake.
    guess = list[mid]
    counter += 1
    print(counter)
    if guess == item:
        return mid
    if guess > item:
        high = mid - 1
    # else:
    #     low = mid + 1 --> I removed this because never is going to enter here!
 return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, -1))

"""
Suppose you have a sorted list of 128 names, and you’re searching
through it using binary search. What’s the maximum number of
steps it would take?
R// 7

 Suppose you double the size of the list. What’s the maximum
number of steps now?
R// 8
"""

#