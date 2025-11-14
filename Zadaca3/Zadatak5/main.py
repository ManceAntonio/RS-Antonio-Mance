import shop.proizvodi as proizvodi
import shop.narudzbe as narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100},
]

for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

for p in proizvodi.skladiste:
    p.ispis()

naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
]

narudzba = narudzbe.napravi_narudzbu(naruceni_proizvodi)

if narudzba:
    narudzba.ispis_narudzbe()
