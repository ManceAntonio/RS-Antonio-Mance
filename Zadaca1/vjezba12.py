def obrni_rjecnik(rjecnik):
    obrnuti = {}
    for kljuc, vrijednost in rjecnik.items():
        obrnuti[vrijednost] = kljuc
    return obrnuti


rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))