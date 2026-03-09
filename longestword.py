

def find_longest_word(long_sentence):
    longest=""
    #print(long_sentence.split())
    word = long_sentence.split()

    #print(len(word))
    for w in word:
        #print(w)
        if len(w)>len(longest):
            longest=w
    
    return longest
    
    


long_sentence="The iswwwwwww a test"
print(find_longest_word(long_sentence))