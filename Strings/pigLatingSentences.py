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