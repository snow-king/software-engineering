import re
from functools import reduce


class Num(object):
    sumNumbers = 0
    multiplyNumbers = 1

    def __init__(self):
        self.numbers = []

    # I know what is so stupid , but I needed to add this method :D
    def sum(self):
        self.sumNumbers = sum(self.numbers)

    # I now what in Python 3.0+ not recommended use reduce, but this is more convenient than writing it all through a
    # loop
    def multiplication(self):
        self.multiplyNumbers = reduce(lambda x, y: x * y, self.numbers)

    def getNumbers(self):
        print("Please, enter a sequence of numbers separated by a space \nExample: 1 2 3 4 5")
        answer = input() + ' '
        # print(re.search(r'[a-zA-Z]+', answer))
        if re.match(r'\d+\s+', answer) and not re.search(r'[a-zA-Z]+', answer):
            self.numbers = list(map(int, answer.split()))
            print(self.numbers)
        else:
            self.getNumbers()

    def run(self):
        self.getNumbers()
        print("Please select : \n1. Sum \n2. Multiplication")
        answer = str(input())
        if answer == "1":
            self.sum()
            print(self.sumNumbers)
        elif answer == "2":
            self.multiplication()
            print(self.multiplyNumbers)
        else:
            print("unknown request (｡╯︵╰｡) \nplease enter correct data ")


example = Num()
example.run()
