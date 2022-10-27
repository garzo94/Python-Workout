"""item is our number to guess inside the list,
returning the index value where the number was found"""

def binary_search(mylist, item):
    # low index in our list
    low = 0
    # high index in our list
    high = len(mylist) - 1

    while low <= high:
        mid = (low + high) // 2 # middle index value in the list
        guess = mylist[mid] # guess number

        # return index if guess number = item
        if guess == item:
            return mid
        # if guess number is higher than item, discards all the subsequent numbers
        if guess > item:
            high = mid - 1
        # otherwise discards all the previous numbers
        else:
            low = mid + 1
    # return None if value does not exist
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 5))

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
