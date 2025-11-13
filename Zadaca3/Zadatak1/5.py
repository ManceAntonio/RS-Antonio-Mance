def paran_broj(x):
    return True if x % 2 == 0 else None

paran_broj_lambda = lambda x: True if x % 2 == 0 else None

broj = int(input("Unesite broj: "))
print(paran_broj_lambda(broj))