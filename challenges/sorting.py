
def usage():
    print("Sorting takes 2 arguments, a list and a string container order asc|desc|none")

def sorting(numbers, order):
    if order == "asc":
        print(sorted(numbers))
        exit
    elif order == "desc":
        print(sorted(numbers,reverse=True))
        exit
    elif order == "none":
        print(numbers)
        exit
    else:
        usage()
        exit

sorting(["a","j","c","y","r","l"],"desc")