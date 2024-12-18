print("sjema")
print("https://github.com/PreVoxX/pythonek-project.git")

n=int(input("podaj n"))
suma=0
for i in range(1, n+1):
    suma+=1
print(suma)

def suma_rekurencyjna(n):
    if n==0:
        return 0
    return n+suma_rekurencyjna(n-1)
print(suma_rekurencyjna(n))
