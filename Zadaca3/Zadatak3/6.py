import math

faktorijeli = {
    n: [math.factorial(k) for k in range(1, n + 1)]
    for n in range(1, 11)
}
print(faktorijeli)
