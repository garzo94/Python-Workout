def mysum(*items):
    if not items:
        return items
    output = items[0]
    for i in items[1:]:
        output += i
    return output

print(mysum(1,2,3))