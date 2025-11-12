import random

number = random.randint(1,100) #gets a random number between the value
attempts = 0

while True :
	
	guess = int(input("guess a number between 1 and 100\n"))
	
	if guess == number:
		print(f"You Guessed Correctly in {attempts} attempts")  	
		break; 	

	else:
		attempts += 1
		if guess < number:
			print("Too Low")
		else:
			print("Too High")

	



