
vowels = ["a", "e", "i", "o", "u"]

def countvowel(string):
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    print(count)

countvowel("aaaaaaau")
