import random
import logging

(logging.basicConfig(level=logging.DEBUG,filename="logs.log",filemode="w", format="%(asctime)s:%(levelname)s - %(message)s"))

job_list = {
 "Java developer":
 {"salary":50, "gladness_less": 10 },
 "Python developer":
 {"salary":40, "gladness_less": 3 },
 "C++ developer":
 {"salary":45, "gladness_less": 25 },
 "Rust developer":
 {"salary":70, "gladness_less": 1 },
 }
brands_of_car = {
 "BMW":{"fuel":100, "strength":100,
 "consumption": 6},
 "Lada":{"fuel":50, "strength":40,
 "consumption": 10},
 "Volvo":{"fuel":70, "strength":150,
 "consumption": 8},
 "Ferrari":{"fuel":80, "strength":120,
 "consumption": 14},
 }

class Human:
    def __init__(self,name="Human",job=None,home=None,car=None):
        logging.debug("base")
        self.name = name
        self.money = 120
        self.gladness = 60
        self.satiety = 60
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        logging.debug("get_home")
        self.home = House()

    def get_car(self):
        logging.debug("get_car")

        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        logging.debug("get_job")
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            logging.debug("I wont to eat")
            self.shopping("food")
        else:
            logging.debug("I'm full")
            if self.satiety >= 100:
                self.satiety = 100

        return
        self.satiety += 5
        self.home.food -= 5

    def work(self):
        if self.car.drive():
            logging.debug("pass car")
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                logging.debug("go work")
                return
            else:
                self.to_repair()
                logging.debug("to repair car")
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 3

    def shopping(self, manage):
        if self.car.drive():
            logging.debug("pass car to go shopping")
            pass
        else:
            if self.car.fuel < 20:
                logging.debug("manage fuel")
                manage = "fuel"
            else:
                logging.debug("repair in shopping")
                self.to_repair()
                return
            if manage == "fuel":
                logging.debug("I bought fuel")
                print("I bought fuel")
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                logging.debug("Bought food")
                print("Bought food")
                self.money -= 60
                self.home.food += 65
            elif manage == "delicacies":
                logging.debug("Hooray! Delicious!")
                print("Hooray! Delicious!")
                self.gladness += 8
                self.satiety += 2
                self.money -= 13

    def chill(self):
        self.gladness += 8
        self.home.mess += 6

    def clean_home(self):
        self.gladness -= 7
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 110
        self.money -= 75

    def days_indexes(self, day):
        day = f" Today the {day} of{self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name +"'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            logging.debug("Depression…!")
            print("Depression…")
            return False
        if self.satiety < 0:
            logging.debug("Dead…!")
            print("Dead…")
            return False
        if self.money < -550:
            logging.debug("Bankrupt…!")
            print("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            logging.debug("is alive false")
            return False
        if self.home is None:
            logging.debug("Settled in the house")
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            logging.debug(f"I bought a car mark")
            self.get_car()
            print(f"I bought a car")
        if self.job is None:
            logging.debug(f"I don't have a job,going to get a job with salary")
            self.get_job()
            print(f"I don't have a job,going to get a job with salary")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            logging.debug("I'll go eat")
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                logging.debug("I want to chill, butt here is somuch mess…\nSo I will clean the house")
                print("I want to chill, butt here is somuch mess…\nSo I will clean the house")
                self.clean_home()
            else:
                logging.debug("Let`s chill!")
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            logging.debug("Start working")
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            logging.debug("I need to repair my car")
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            logging.debug("Let`s chill!")
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            logging.debug("Start working")
            print("Start working")
            self.work()
        elif dice == 3:
            logging.debug("Cleaning time!")
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            logging.debug("Time for treats!")
            print("Time for treats!")
            self.shopping(manage="delicacies")
class Auto:
    def __init__(self, brand_list):
         self.brand = random.choice(list(brand_list))
         self.fuel = brand_list[self.brand]["fuel"]
         self.strength = brand_list[self.brand]["strength"]
         self.consumption =brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            logging.debug("drive True")
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            logging.debug("The car cannot move")
            print("The car cannot move")
            return False
class House:
    def __init__(self):
     self.mess = 0
     self.food = 0

class Job:
     def __init__(self, job_list):
         self.job = random.choice(list(job_list))
         self.salary = job_list[self.job]["salary"]
         self.gladness_less = job_list[self.job]["gladness_less"]
nick = Human(name="Nick")

day=0
while nick.live(day)!=False:
    day+=1
print("Count day survive is:",day)

