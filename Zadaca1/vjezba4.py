brojac = 0
while True:
    broj = int(input("Unesi cijeli broj: "))
    if broj == 0:
        break
    brojac += broj
print(f"Zbroj svih brojeva je {brojac}")
