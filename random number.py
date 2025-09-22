import random 

low = 10 
high = 18 
# options = ["rock", "paper", "scissors"]   >> for this line, option = random.choice(options)   
# options = ("rock", "paper", "scissors")   >> for this line, option = random.choice(options)  
options = {"rock", "paper", "scissors"}    #>> for this line, option = random.choice(list(options)) 
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(list(options))
random.shuffle(cards)

print(cards)