def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    broj_samoglasnika = 0
    broj_suglasnika = 0

    for znak in tekst:
        if znak in vowels:
            broj_samoglasnika += 1
        elif znak in consonants:
            broj_suglasnika += 1

    return {"vowels": broj_samoglasnika, "consonants": broj_suglasnika}

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))