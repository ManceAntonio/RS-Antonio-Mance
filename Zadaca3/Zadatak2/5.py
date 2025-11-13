rijeci = [
    "jabuka", "pas", "knjiga", "zvijezda", "prijatelj",
    "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"
]

min_duljina = int(input("Unesite minimalnu duljinu riječi: "))

duge_rijeci = list(filter(lambda r: len(r) > min_duljina, rijeci))
print(duge_rijeci)
