"""Vehacle"""


class Vehacle:
    """ Main class Vehacle"""
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        """get info"""
        return f"Make is {self.make}, model is {self.model}"


class Car(Vehacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


class Moto(Vehacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


car = Car("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR600RR", 2)

print(car.get_info())
print(moto.get_info())
