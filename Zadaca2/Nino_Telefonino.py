POZIVNI = {
    "01":  ("Grad Zagreb i Zagrebačka županija", "fiksna mreža", None),
    "020": ("Dubrovačko-neretvanska županija",   "fiksna mreža", None),
    "021": ("Splitsko-dalmatinska županija",     "fiksna mreža", None),
    "022": ("Šibensko-kninska županija",         "fiksna mreža", None),
    "023": ("Zadarska županija",                 "fiksna mreža", None),
    "031": ("Osječko-baranjska županija",        "fiksna mreža", None),
    "032": ("Vukovarsko-srijemska županija",     "fiksna mreža", None),
    "033": ("Virovitičko-podravska županija",    "fiksna mreža", None),
    "034": ("Požeško-slavonska županija",        "fiksna mreža", None),
    "035": ("Brodsko-posavska županija",         "fiksna mreža", None),
    "040": ("Međimurska županija",               "fiksna mreža", None),
    "042": ("Varaždinska županija",              "fiksna mreža", None),
    "043": ("Bjelovarsko-bilogorska županija",   "fiksna mreža", None),
    "044": ("Sisačko-moslavačka županija",       "fiksna mreža", None),
    "047": ("Karlovačka županija",               "fiksna mreža", None),
    "048": ("Koprivničko-križevačka županija",   "fiksna mreža", None),
    "049": ("Krapinsko-zagorska županija",       "fiksna mreža", None),
    "051": ("Primorsko-goranska županija",       "fiksna mreža", None),
    "052": ("Istarska županija",                 "fiksna mreža", None),
    "053": ("Ličko-senjska županija",            "fiksna mreža", None),
    "091": (None, "mobilna mreža", "A1 Hrvatska"),
    "092": (None, "mobilna mreža", "Tomato"),
    "095": (None, "mobilna mreža", "Telemach"),
    "097": (None, "mobilna mreža", "bonbon"),
    "098": (None, "mobilna mreža", "Hrvatski Telekom"),
    "099": (None, "mobilna mreža", "Hrvatski Telekom"),
    "0800": (None, "posebne usluge", None),
    "060":  (None, "posebne usluge", None),
    "061":  (None, "posebne usluge", None),
    "064":  (None, "posebne usluge", None),
    "065":  (None, "posebne usluge", None),
    "069":  (None, "posebne usluge", None),
    "072":  (None, "posebne usluge", None),
}

def _ocisti_broj(broj: str) -> str:
    rezultat = []
    for ch in broj:
        if ch.isdigit() or ch == "+":
            rezultat.append(ch)
    return "".join(rezultat)

def _u_nacionalni_oblik(broj: str) -> str | None:
    if not broj:
        return None

    if broj.startswith("+"):
        broj = broj[1:]

    if broj.startswith("00385"):
        broj = broj[5:]
    elif broj.startswith("385"):
        broj = broj[3:]

    if not broj.isdigit():
        return None

    if not broj.startswith("0"):
        broj = "0" + broj

    return broj

def _pronađi_pozivni_broj(nacionalni: str) -> str | None:
    for duljina in (4, 3, 2):
        if len(nacionalni) >= duljina:
            pref = nacionalni[:duljina]
            if pref in POZIVNI:
                return pref
    return None

def validiraj_broj_telefona(broj: str) -> dict:
    rezultat = {
        "pozivni_broj": None,
        "broj_ostatak": None,
        "vrsta": None,
        "mjesto": None,
        "operater": None,
        "validan": False,
    }

    cisti = _ocisti_broj(broj)
    nacionalni = _u_nacionalni_oblik(cisti)
    if nacionalni is None or not nacionalni.isdigit():
        return rezultat

    pozivni = _pronađi_pozivni_broj(nacionalni)
    if pozivni is None:
        rezultat["broj_ostatak"] = nacionalni
        return rezultat

    rezultat["pozivni_broj"] = pozivni
    ostatak = nacionalni[len(pozivni):]
    rezultat["broj_ostatak"] = ostatak

    mjesto, vrsta, operater = POZIVNI[pozivni]
    rezultat["vrsta"] = vrsta

    if vrsta == "fiksna mreža":
        rezultat["mjesto"] = mjesto
        rezultat["operater"] = None
        if ostatak.isdigit() and len(ostatak) in (6, 7):
            rezultat["validan"] = True

    elif vrsta == "mobilna mreža":
        rezultat["mjesto"] = None
        rezultat["operater"] = operater
        if ostatak.isdigit() and len(ostatak) in (6, 7):
            rezultat["validan"] = True

    elif vrsta == "posebne usluge":
        rezultat["mjesto"] = None
        rezultat["operater"] = None
        if ostatak.isdigit() and len(ostatak) == 6:
            rezultat["validan"] = True

    return rezultat

def main():
    broj = input("Unesite broj telefona: ")
    rezultat = validiraj_broj_telefona(broj)
    print(f"Pozivni broj: {rezultat['pozivni_broj']}")
    print(f"Broj ostatak: {rezultat['broj_ostatak']}")
    print(f"Vrsta: {rezultat['vrsta']}")
    print(f"Mjesto: {rezultat['mjesto']}")
    print(f"Operater: {rezultat['operater']}")
    print(f"Validan: {rezultat['validan']}")

if __name__ == "__main__":
    main()