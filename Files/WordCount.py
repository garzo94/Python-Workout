def wordcount(filename):
    counts = {'characters': 0,'words': 0,'lines': 0}
    unique_words = set() # creating a set {}
    for one_line in open(filename):
        counts['lines'] += 1 # counting lines
        counts['characters'] += len(one_line) # counting characters even spaces
        counts['words'] += len(one_line.split()) # counting words with len of a list
        print(unique_words)
        unique_words.update(one_line.split()) # is like append but update with new values that are entering
        counts['unique words'] = len(unique_words) # couting words
    # for key, value in counts.items():
        # print(f'{key}: {value}')
wordcount('WordCount.txt')