# returning multiples values
def ooperation():
    return False, -1


b, n = ooperation()


# arguments##########################
def show_names(*names, **params):  # *name is a tuple
    print(names[0])
    print(params)


show_names('alex', 'jorge', minombre='alex')
# alex
# {'minombre': 'alex'}

# recursion! ############################
# every problem tha can be solved with iteration can be solved with recursion as well.

# global variables
c= 0
def test():
    global c
    c = 15
    return c +20



