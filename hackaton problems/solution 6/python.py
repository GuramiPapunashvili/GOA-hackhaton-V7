def removeLetter(word, toRemove):
    result = []
    for i in word:
        if i == toRemove:
            continue
        else:
            result.append(i)
    return ''.join(result)

print(removeLetter('hello', 'l'))       