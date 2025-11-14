import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self): return self.a + self.b
    def oduzimanje(self): return self.a - self.b
    def mnozenje(self): return self.a * self.b
    def dijeljenje(self): return self.a / self.b if self.b != 0 else "Ne može"
    def potenciranje(self): return self.a ** self.b
    def korijen(self): return math.sqrt(self.a) if self.a >= 0 else "Negativan broj"

k = Kalkulator(10, 5)
print(k.zbroj())
print(k.korijen())
