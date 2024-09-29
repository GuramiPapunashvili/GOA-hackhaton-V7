def repeated(word):
    for i in word:
        if word.count(i) == 2:
            return True
    return False

print(repeated([4,4,3,3,2,9,4]))