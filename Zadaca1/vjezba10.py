def brojanje_rijeci(tekst):
    rijeci = tekst.split()
    rezultat = {}
    for rijec in rijeci:
        if rijec in rezultat:
            rezultat[rijec] += 1
        else:
            rezultat[rijec] = 1
    return rezultat

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_rijeci(tekst))
