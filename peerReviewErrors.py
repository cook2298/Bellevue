# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jacob Cook
# Creation Date: 10/12/2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
	cave = ''						#1.) spaces were used here instead of a tab to seprate the block. Must be either or. I chose to backspace and use a tab.
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
	return cave						#2.) return was 'caves' with an 's'. 'cave' is what really needs to be returned. 
									
def checkCave(chosenCave):			
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds			
	time.sleep(2)					#3.) comment says 2 seconds for the timer, but 3 was the arg passed to sleep() - changed to 2 to match comment
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)
	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')  		#4.) print requires () 
														#5.) not an error, but bad practice to have processing outside of a defined method
def main():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':		#6.) while loop needs comparison operator, not assignment operator. == not = 
		displayIntro()
		caveNumber = chooseCave()						#7.) choosecave() is not the same as the defined choseCave() capitialization matters! 
		checkCave(caveNumber)
    
		print('Do you want to play again? (yes or no)')
		playAgain = input()
		if playAgain != 'yes' and playAgain != 'y':		#8.) if you want this message to display every time they leave, might be bettter to have the condition be 'not yes'
			print("Thanks for playing")					#9.) spelling error. planing changed to playing

main()