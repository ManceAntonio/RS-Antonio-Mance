class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(self.marka, self.model, self.godina_proizvodnje, self.kilometraza)

    def starost(self):
        import datetime
        print(datetime.datetime.now().year - self.godina_proizvodnje)

auto = Automobil("Ford", "Focus", 2013, 150000)
auto.ispis()
auto.starost()
