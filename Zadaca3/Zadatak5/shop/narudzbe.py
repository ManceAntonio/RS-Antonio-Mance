from shop import proizvodi

narudzbe = []


class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        tekst = ", ".join(
            f"{p['naziv']} x {p['narucena_kolicina']}"
            for p in self.naruceni_proizvodi
        )
        print(f"Naručeni proizvodi: {tekst}, Ukupna cijena: {self.ukupna_cijena} eur")


def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list):
        print("Greška: naruceni_proizvodi mora biti lista!")
        return None

    if len(naruceni_proizvodi) == 0:
        print("Greška: lista naručenih proizvoda je prazna!")
        return None

    for p in naruceni_proizvodi:
        if not isinstance(p, dict):
            print("Greška: svaki element mora biti rječnik!")
            return None
        if not {"naziv", "cijena", "narucena_kolicina"}.issubset(p.keys()):
            print("Greška: rječnik mora sadržavati ključeve: naziv, cijena, narucena_kolicina!")
            return None

    for naruceni in naruceni_proizvodi:
        naziv = naruceni["naziv"]
        kolicina = naruceni["narucena_kolicina"]

        proizvod = next((x for x in proizvodi.skladiste if x.naziv == naziv), None)
        if proizvod is None or proizvod.dostupna_kolicina < kolicina:
            print(f"Proizvod {naziv} nije dostupan!")
            return None

    for naruceni in naruceni_proizvodi:
        proizvod = next((x for x in proizvodi.skladiste if x.naziv == naruceni["naziv"]), None)
        proizvod.dostupna_kolicina -= naruceni["narucena_kolicina"]

    ukupna_cijena = sum(
        p["cijena"] * p["narucena_kolicina"] for p in naruceni_proizvodi
    )

    nova = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append({"narudzba": nova})
    return nova
