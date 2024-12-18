import random
pętla = 0
while pętla ==0:

   print("Wybierz jeden z poniższych ruchów:")
   print(" papier")
   print(" kamien")
   print(" nozyce")

   wybór = input("wybierasz : ")

   komputer = random.choice(["papier", "kamien", "nozyce"])

   if wybór not in ["papier", "kamien", "nozyce"]:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
      

   komputer = random.choice(["papier", "kamien", "nozyce"])

   print(f"Komputer wybrał: {komputer}")

   if wybór == komputer:
         print ("Remis!")
   elif (wybór == "papier" and komputer == "kamien") or \
          (wybór == "kamien" and komputer == "nozyce") or \
          (wybór == "nozyce" and komputer == "papier"):
             print ("Wygrałeś!")
   else:
               print("Przegrałeś!")

   pętla=int(input("wybierz 0 jeśli chcesz kontynuowac"))