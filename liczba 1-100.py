import random

wylosowana_liczba = random.randint(1, 100)

print("Komputer wylosował liczbę od 1 do 100")
print("Musisz zgadnąć tę liczbę")
print("Komputer powie ci czy Twoja liczba jest za mała za duża lub poprawna")

proby = 0

while True:
    zgadywana_liczba = int(input("Podaj swoją propozycję liczby: "))
    proby += 1 
    
    if zgadywana_liczba < wylosowana_liczba:
        print("Za mała! Spróbuj zgadnąć większą liczbę")
    elif zgadywana_liczba > wylosowana_liczba:
        print("Za duża! Spróbuj zgadnąć mniejszą liczbę")
    else:
        print(f"Brawo! Zgadłeś liczbę {wylosowana_liczba} w {proby} próbach")
        break