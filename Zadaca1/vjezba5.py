for i in range(1, 2):
  print(i)
# Primjer nema smisla jer se for koristi kad zelimo ponavljati više puta, 
# ova petlja se izvršava samo jednom i ispisuje 1 a isto je kao i da je napisano
# print (1) jer primjer ne koristi smisao petlje.

for i in range(10, 1, 2):
  print(i)
# Nece se nista ispisati jer 10 ne može doći do 1 ako brojac ide +2
# Moglo bi se doci do 1 ali ne ukljucujuci 1 da pise 
# for i in range(10, 1, -2):
# rezultat bi ispisao brojeve 10,8,6,4,2

for i in range(10, 1, -1):
  print(i)
# ispisuju se brojevi od 10 do 2 jer je u petlji stavljeno da krene od 10 i da dode do 1 za -1.
