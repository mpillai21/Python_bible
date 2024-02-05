# get sentence
original=input("Give me a sentence for the piggy business!-->").strip().lower()
# split the sentence into words
words=original.split()
# loop through the words and convert
new_words=[]
for w in words:
    if w[0] in "aeiou":
        new_word=w+ "yay"
        new_words.append(new_word)
    else:
        i=0
        for letter in w:
            if letter not in "aeiou":
                i=i+1
            else:
                break
        cons=w[:i]
        the_rest=w[i:]
        new_word=cons+the_rest+"ay"
        new_words.append(new_word)
# stick the words back to the sentence
output=" ".join(new_words)
# out
print(output)
