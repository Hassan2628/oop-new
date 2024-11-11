
#The cat enitity
class Cat:
    #The constructor:
    #The constructor will create a cat for us in code
    #To create a cat, we need given_name and given_colour
    #self is the cat we are creating.
    def __init__(self, given_name, given_colour):
        self.name = given_name
        #Name attribute
        self.colour = given_colour
        #Colour attribute
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    def train(self):
        print(f"{self.name} is training....")
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1
    def feed(self):
        print(f"{self.name} is eating....")
        self.energy += 10
        self.intelligence += 1
        self.age += 0.1
    def sleep(self):
        print(f"{self.name} is sleeping....
              ")
        self.energy += 10
        self.intelligence += 0
        self.age += 0.1
    def play(self):
        print(f"{self.name} is playing....")
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1 
    def print_stats(self):
        print(f"""
              Here is {self.name}'s stats
    Age : {self.age} 
    Energy : {self.energy} 
    Intelligence : {self.intelligence} 
    Weight : {self.weight} """)

        
