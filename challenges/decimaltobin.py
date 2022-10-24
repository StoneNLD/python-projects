

def convert(d):
    if d <= 1024:
        print(bin(d))
    else:
        print("Decimal value need be <= 1024")

convert(50)