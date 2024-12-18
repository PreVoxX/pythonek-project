
n = int(input("Podaj liczbę:"))

if n < 2:
    print("Liczba nie jest pierwsza")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Liczba nie jest pierwsza")
            break
    else:
        print("Liczba jest pierwsza")