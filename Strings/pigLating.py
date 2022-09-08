# my solution
def pig_lating(word):
    isvowel = word[0] in 'aeiou'
    if isvowel:
        pigWord = word +'way'
        return pigWord
    else:
        first_letter = word[0]
        pigWord = word[1:]+first_letter+'ay'
        return pigWord
# book solution
# def pig_latin(word):
#     if word[0] in 'aeiou':
#         return f'{word}way'
#     return f'{word[1:]}{word[0]}ay'
#
# print(pig_latin('python'))





