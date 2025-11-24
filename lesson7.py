class Animal:
    def __init__(self, name, color, nutrition, size):
        self.name = name
        self.color = color
        self.nutrition = nutrition
        self.size = size
        
    def __str__(self):
        return f'Название:{self.name}\nЦвет:{self.color}\nПитание:{self.nutrition}\nРазмер:{self.size}'
    
Animal_1 = Animal(name="Lion", color='orange', nutrition='meat', size='130s')

class WaterAnimal(Animal):
    def __init__(self, name, color, nutrition, size):
        super().__init__(name, color, nutrition, size)
        
    def swim(self):
        return f"{self.name} хорошо плавает!"

water_Animal = WaterAnimal(name='tiger shark', color='blue', nutrition='fish and meat', size='3m')


    
class LandAnimal(Animal):
    def __init__(self, name, color, nutrition, size):
        super().__init__(name, color, nutrition, size)
        
    def run(self):
        return f"{self.name} быстро бегает!"
        
land_Animal = LandAnimal(name='panter', color='yellow', nutrition='meat', size='1,5m')


class AirAnimal(Animal):
    def __init__(self, name, color, nutrition, size):
        super().__init__(name, color, nutrition, size)
        
    def fly(self):
        return f"{self.name} высоко летает!"
        
air_Animal = AirAnimal(name='crow', color='black', nutrition='meat', size='0.5m')


print(Animal_1, "\n")
print(water_Animal, "\n", water_Animal.swim(), "\n")
print(land_Animal, "\n", land_Animal.run(), "\n")
print(air_Animal, "\n", air_Animal.fly(), "\n")