import random
job_list = {
    "JS":{"salary":100,"gladness_list":10},
    "Python":{"salary":80,"gladness_less":3},
    "C++":{"salary":90,"gladness_less":1},
}

brands_of_car = {
    "Volkswagen":{"fuel":100,"strength":100,"cunsumption":6}
}

class Human:
    def __init__(self,name,job=None,home=None,car=None):
        self.name = name
        self.money = 100
        self.gladness = 100
        self.job = job
        self.car = car
        self.home = home
    def get_home(self):
        pass
    def get_car(self):
        pass
    def job(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def days_index(self):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass

class Auto:
    def __init__(self,brand_list):
        self.brand=random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.cunsumption = brand_list[self.brand]["cunsumption"]
    def __init__(self):
        self.mess = 0
        self.salary = 0
class Job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

person = Human(name="Nick")