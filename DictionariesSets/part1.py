import string
def gematria_dict():
    return {char: index for index, char in enumerate(string.ascii_lowercase,1)}

print(list(enumerate('abcdefghijklmn',1)))