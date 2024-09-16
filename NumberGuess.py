import random
class NumberGuess:
    
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guess = -1
        
    def play(self):
        while (self.number != self.guess):
            value = input("Guess a number from 1 to 100: ")
            self.guess = int(value)
            if (self.guess < self.number):
                print("Too low")
            elif (self.guess > self.number):
                print("Too high")
            else:
                print("You guessed the number!")
                
game = NumberGuess()
game.play()