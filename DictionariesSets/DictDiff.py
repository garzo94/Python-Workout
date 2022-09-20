import operator
def dictdiff(dict1, dict2):
    result = {}
    for obj1, obj2 in zip(dict1, dict2):
        if dict1[obj1] == dict2[obj2]:
            pass
        elif dict1[obj1] != dict2[obj2] and obj1 == obj2:
            result[obj1] = [dict1.get(obj1), dict2.get(obj2)]
        elif dict1[obj1] != dict2[obj2] and obj1 != obj2:
            result[obj1] = [None,dict1.get(obj1)]
            result[obj2] = [dict2.get(obj2),None]
    return dict(sorted(result.items())) # sorting by key




d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}
# print(dictdiff(d3,d4))

def dictdiff2(first, second):
    output = {}
    all_keys = first.keys() | second.keys()
    print(all_keys)
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key),
        second.get(key)]
    return output

print(dictdiff2(d1, d2))
