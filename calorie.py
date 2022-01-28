
from temperature import Temperature
# Calorie class represents optimal daily calorie intake
class Calorie :

    def __init__(self, weight, height, age, temperature) :
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age
# calculation of daily calorie intake base on this eqation
    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return  str(result)



if __name__ == "__main__":
    temperature = Temperature(country="serbia", city="belgrade").get()
    calorie = Calorie( weight =70, height =175,age =22, temperature = temperature)
    print(calorie.calculate())