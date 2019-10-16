spam = ['apples', 'pizza', 'dogs', 'cats']

def grammar(words):
    for i in range(len(words) -2):
        print(words[i], end = ", ")
    print(words[-2] + ', and ' + words[-1]) 

grammar(spam)
