from datetime import datetime
from  dateutil.relativedelta import relativedelta

class Human():
    def __init__(self, year, month, day):
        self.birthday = datetime(year, month, day)

    def get_age(self):
        return relativedelta(datetime.now(), self.birthday).years


if __name__ == '__main__':
    humans = []
    humans.append(Human(2020, 1, 10))
    humans.append(Human(2013, 5, 10))
    humans.append(Human(2010, 1, 20))
    humans.append(Human(1970, 3, 30))

    for human in humans:
        print(human.get_age())
