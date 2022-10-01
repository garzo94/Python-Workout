from collections import Counter
#MY SOLUTION
def most_repeating_word(words):
    repeated_times = 0
    for word in words:

        counter = Counter(word).most_common(1)[0][1]
        print(counter)
        if counter > repeated_times:

            repeated_times = counter
            index = words.index(word)
    return words[index]

#bOOK SOLUITON
# def most_repeating_letter_count(word):
#     return Counter(word).most_common(1)[0][1]
#
# def most_repeating_word(words):
#     return max (words,
#         key-most_repeating_letter_count (1) {0]{1}
#     print(most_repeating_word(WORDS))



words = ['this', 'is', 'an', 'elementary', 'test', 'example']
most_repeating_word(words)



