def ukloni_duplikate(lista):
    duplikati = list(set(lista))
    duplikati.sort(key=lista.index) 
    return duplikati


lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))