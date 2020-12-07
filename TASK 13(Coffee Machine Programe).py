#Best Enlist Python Internship

#First OOP Project
class CoffeeMachine:

    running = False
    
    def __init__(self, water, milk, coffee_beans, cups, money):
        # quantities of items the coffee machine already had
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        
        #if the machine isnt running then start running
        if not CoffeeMachine.running:
            self.start()

    def start(self):
        self.running = True # it is running as to not trigger the start() in initialiser method
        self.payment = input("Enter payment here. Accepted coins ( quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 ): ").split(",")
        "Enter payment here. Accepted coins ( quarters = $4, dimes = $2, nickles = $1, pennies = $1 ): ".split(","))
        print()
        #possible choices to perform in the coffee machine
        if self.payment in action_choices:
            action_choices[self.action]()
        else:
            exit()

    def return_to_menu(self): # returns to the menu after an action
        print()
        self.start()

    def available_check(self): # checks if it can afford making that type of coffee at the moment
        self.not_available = "" # by checking whether the supplies goes below 0 after it is deducted
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee - self.reduced[2] < 0:
            self.not_available = "coffee"
        
        if self.not_available != "": # if something was detected to be below zero after deduction
            print(f"Sorry, not enough {self.not_available}!")
            return False
        else: # if everything is enough to make the coffee
            print("I have enough resources, making you a coffee!")
            return True

    def deduct_supplies(self): # performs operation from the reduced list, based on the coffee chosen
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee -= self.reduced[2]
        self.money += self.reduced[4]

    def buy(self):
        self.choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.payment = input("What type of coin ? Quarter, Dimes, nickles, pennies ")
            if self.choice == '1':
            self.reduced = [250, 0, 96, 2.5] # water, milk, coffee, money
                if self.available_check(): # checks if supplies are available
                self.deduct_supplies() # if it is, then it deducts

            elif self.choice == '2':
            self.reduced = [100, 50, 76, 2.5]
                if self.available_check():
                self.deduct_supplies()

            elif self.choice == "3":
            self.reduced = [200, 100, 72, 5]
                if self.available_check():
                self.deduct_supplies()

            elif self.choice == "back": # if the user changed his mind
            self.return_to_menu()
            

        self.return_to_menu()

    def fill(self): # for adding supplies to the machine
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee += int(input("Write how many grams of coffee powder do you want to add:\n"))
        self.return_to_menu()

    def take(self): # for taking the money from the machine
        print(f"I gave you ${self.money}")
        self.money -= self.money
        self.return_to_menu()

    def status(self): # to display the quantities of supplies in the machine at the moment
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee")
        print(f"${self.money} of money")
        self.return_to_menu()

CoffeeMachine(300, 200, 100, 500) # specify the quantities of supplies at the beginning
            # water, milk, coffee, money
        print("here is your /coffee.Enjoy!")
        
