# 1. for petlja
suma = 0
for i in range(2, 101, 2):
    suma += i
print("Suma parnih brojeva:", suma)

# 1. while petlja
suma = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        suma += i
    i += 1
print("Suma parnih brojeva:", suma)

# 2. for petlja
neparni = []
for i in range(1, 20, 2):
    neparni.append(i)
neparni.reverse()
print("Neparni brojevi:", neparni)

# 2. while petlja
neparni = []
broj = 1
while len(neparni) < 10:
    if broj % 2 == 1:
        neparni.append(broj)
    broj += 1
neparni.reverse()
print("Neparni brojevi:", neparni)

# 3. for petlja
fib = [0, 1]
for i in range(2, 1000):
    novi = fib[-1] + fib[-2]
    if novi > 1000:
        break
    fib.append(novi)
print("Fibonaccijev niz:", fib)

# 3. while petlja
fib = [0, 1]
while True:
    novi = fib[-1] + fib[-2]
    if novi > 1000:
        break
    fib.append(novi)
print("Fibonaccijev niz:", fib)