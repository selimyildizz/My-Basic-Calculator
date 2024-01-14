import math

class Calculator:
    def __init__(self) -> None:
        pass

    def add(self, a, b):
        # result will be adding of a and b
        return a+b
    
    def sub(self, a, b):
        # result will be subtraction of a and b
        return a-b
    
    def run(self):
        # print methods
        print("1: add\n2: sub (work in progress will be upgraded on next commit)")
        
        # get choice
        choice = int(input("your choice: "))

        # choice 1 = add

        if choice == 1:
            # do add
            self.choice_add()

    def choice_add(self):
        while True:
            try:
                # get first number
                a_value = int(input("first number: "))
                
                # get second number
                b_value = int(input("second number: "))

                # print result
                print("your result: " + str(self.add(a_value, b_value)))
                
                # break loop
                break
            except ValueError:
                pass

    def loop(self):
        # print welcome message
        print("welcome to my calculator:\n")
        
        while True:
            try:
                # run loop
                self.run()
            # break loop if keyboard interrupt
            except KeyboardInterrupt:
                break

my_calculator = Calculator()
my_calculator.loop()