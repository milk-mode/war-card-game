
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        return "Vehicle starts"
    def stop(self):
        return "Vehicle stops"
    def fuel_up(self):
        return "Vehicle fuels up"
   
class Car(Vehicle):
    def __init__(self, make, model, year,num_doors):
        super().__init__(make, model, year)
        self.num_doors=num_doors
    def honk(self):
        return "honk"   

class Bicycle(Vehicle):
    def __init__(self, make, model, year,num_gears):
        super().__init__(make, model, year)
        self.num_gears=num_gears
    def ring(self):
        return "ring"
    
car=Car("Toyota",'corolla',2015,4)
cycle=Bicycle("Rex","model x",2015,7)
print(car.start())
print(car.stop())
print(car.honk())
print(cycle.ring())