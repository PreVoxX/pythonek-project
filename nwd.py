a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

def NWD(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

print(f"Największy wspólny dzielnik liczb {a} i {b} to: {NWD(a, b)}") 