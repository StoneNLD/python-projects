

def comparexo(string):
    countx = 0
    counto = 0
    for letter in list(string):
        if letter.upper() == "X":
            countx += 1
        elif letter.upper() == "O":
            counto += 1
    if countx == counto:
        return True
    else:
        return False

print(comparexo("k"))