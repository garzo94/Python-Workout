#my solution
def pig_latin(sentence):
    listSentence = sentence.split() ##Split gives us an array of every word in a sentence
    finalSentence = ''
    for word in listSentence:
        if word[0] in 'aeiou':
            finalSentence += f'{word}way '
        else:
            finalSentence += f'{word[1:]}{word[0]}ay '
    print(finalSentence)

pig_latin('this is a test translation')

#book solution
# def pl_sentence(sentence):
#     output = []
#     for word in sentence.split():
#         if word[0] in 'aeiou':
#             output.append(f'{word}way')
#         else:
#             output.append(f'{word[1:]}{word[0]}ay')
#     return ' '.join(output)
# print(pl_sentence('this is a test'))