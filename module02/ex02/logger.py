import time
from random import randint
from functools import wraps
from datetime import datetime
import getpass


def log(fct):
    @wraps(fct)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = fct(*args, **kwargs)
        total = (datetime.now() - start)
        with open('machine.log', 'a') as log_file:
            if total.total_seconds() >= 1:
                total_str = '{:<4.3f} s '.format(total.total_seconds())
            else:
                total_str = '{:<4.3f} ms'.format(total.microseconds / 1000)
            line = '({})Running: {:<18} [ exec-time = {} ]\n'
            log_file.write(line.format(getpass.getuser(), ' '.join(
                fct.__name__.split('_')).title(), total_str))
        return result
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
