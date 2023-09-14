import random
job_list = {
    "JS":{"salary":100,"gladness_list":10},
    "Python":{"salary":80,"gladness_less":3},
    "C++":{"salary":90,"gladness_less":1},
}

brands_of_car = {
    "Volkswagen":{"fuel":100,"strength":100,"cunsumption":6}
}
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
class Human:
    def __init__(self,name,job=None,home=None,car=None):
        self.name = name
        self.money = 100
        self.gladness = 100
        self.satiety = 100
        self.job = job
        self.car = car
        self.home = home
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food<=0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
        self.satiety += 5
        self.satiety -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
            if manage == "fuel":
                print("I bought fuel")
                self.money-=30
                self.car+=100

            elif manage == "food":
                print("Bought food")
                self.money -= 25
                self.home.food += 50

            elif manage == "delicacies":
                print("nam")
                self.gladness += 10
                self.satiety +=4
                self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.food +=5
        #self.money -= 5
    def clean_home(self):
        self.gladness -=5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 40
    def days_index(self,day):
        day = f"today the{day} of {self.name}'s life'"
        print(f"{day:=^50}","\n")
        human_index = self.name +"'s index'"
        print(f"{human_index}:^50","\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_index = "Home index"
        print(f"{home_index}:=^50","\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_index = f"{self.car.brand}car index"
        print(f"{car_index}:=^50","\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")
    def is_alive(self):
        pass
    def live(self):
        pass

class Auto:
    def __init__(self,brand_list):
        self.brand=random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
class Job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

person = Human(name="Nick")