def joinNumbers(ran):
    mylist = [str(x) for x in range(ran)]
    return ",".join(mylist)

print(joinNumbers(10))

