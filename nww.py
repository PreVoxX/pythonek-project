a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def NWW(a, b):
    if a == 0 or b == 0:
        return 0 
    return abs(a * b) // NWD(a, b)
print(f"Najmniejsza wspólna wielokrotność liczb {a} i {b} to: {NWW(a, b)}")
