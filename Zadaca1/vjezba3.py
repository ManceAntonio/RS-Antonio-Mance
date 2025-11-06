import random

skriveni_broj = random.randint(1, 100)
broj_je_pogoden = False
broj_pokusaja = 0

print("Pogodi broj između 1 i 100!")

while not broj_je_pogoden:
    unos = int(input("Unesite broj: "))
    broj_pokusaja += 1
    if unos == skriveni_broj:
        broj_je_pogoden = True
        print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja.")
    elif unos > skriveni_broj:
        print("Manji je!")
    else:
        print("Veći je!")
