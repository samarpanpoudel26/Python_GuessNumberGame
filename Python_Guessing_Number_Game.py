
#Game Description

#Think a random number myNum between 1 and 100 and play a Number Guessing game with computer.

import random

while True:
	myNum=random.randint(1,100)
	attempt=0
	score=0
 
	while True:
		attempt=attempt+1
			
		#Taking input from user
		Number=int(input("Guess the number between 1 to 100\n>>"))
			
		#Checking the other conditions
		if Number<=0:
			print("Please enter a valid integer number\n>>")
			continue
		elif Number<myNum:
			print("Your guessed number is too low.Please try again")
			continue
		elif Number>myNum:
			print("Your guessing is too high.Please try again")
			continue
		else:
			print("Congratulations.You won")
			score=10-attempt
			print("Your final score is \n",score) #printing user score
			break
	Ask=input("Do you want to play again.yes/no\n>>") #Now asking user for playing again or not
	if Ask.lower()=="yes":
		continue
	else:
		break
   	
   
   
		
	
	
			
			




 



    