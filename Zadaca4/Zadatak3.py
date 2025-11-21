import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik_iz_baze: dict, unesena_lozinka: str):
    print(f"Autorizacija korisnika {korisnik_iz_baze['korisnicko_ime']}...")
    await asyncio.sleep(2)

    lozinka_iz_baze = None
    for zapis in baza_lozinka:
        if zapis['korisnicko_ime'] == korisnik_iz_baze['korisnicko_ime']:
            lozinka_iz_baze = zapis['lozinka']
            break

    if lozinka_iz_baze == unesena_lozinka:
        return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija uspješna."
    return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija neuspješna."

async def autentifikacija(korisnik: dict):
    print("Pokretanje autentifikacije...")
    await asyncio.sleep(3)

    korisnicko_ime = korisnik['korisnicko_ime']
    email = korisnik['email']
    lozinka = korisnik['lozinka']

    korisnik_iz_baze = None
    for zapis in baza_korisnika:
        if zapis['korisnicko_ime'] == korisnicko_ime and zapis['email'] == email:
            korisnik_iz_baze = zapis
            break

    if korisnik_iz_baze is None:
        return f"Korisnik {korisnicko_ime} nije pronađen."

    return await autorizacija(korisnik_iz_baze, lozinka)

async def main():
    unos = {
        "korisnicko_ime": "mirko123",
        "email": "mirko123@gmail.com",
        "lozinka": "lozinka123"
    }

    rezultat = await autentifikacija(unos)
    print(rezultat)

if __name__ == "__main__":
    asyncio.run(main())
