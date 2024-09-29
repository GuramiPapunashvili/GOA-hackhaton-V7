def addAndSubtract(str):
    num = 0
    res = []
    for i in str:
        if i == '+':
            num += 1
            res.append(num)
        elif i == '-':
            num -= 1
            res.append(num)
    return res

print(addAndSubtract('++++------++'))            
