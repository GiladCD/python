def bina (number,bitlen):
    number = ~number+1
    number = format(number & ((1 << bitlen) - 1),f'0{bitlen}b')
    return number
print(bina(int(input("Enter number ")),int(input("Enter bit length "))))