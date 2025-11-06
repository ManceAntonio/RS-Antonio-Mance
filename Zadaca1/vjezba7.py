def provjera_lozinke(lozinka):
    if not (8 <= len(lozinka) <= 15):
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return False

    if not any(z.isupper() for z in lozinka) or not any(z.isdigit() for z in lozinka):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return False

    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return False

    print("Lozinka je jaka!")
    return True


while True:
    lozinka = input("Unesite lozinku: ")
    if provjera_lozinke(lozinka):
        break
