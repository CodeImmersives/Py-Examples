#################
# Author: Oscar Parra
# Email:  ogparra.15@gmail.com
# Date:   7/12/2017
#
# Title: Sequential Search 
# Program Description: 
# Find a min and max number from a randomly generated array
# of size N. Where N is some integer specified by the user.
#################

import random 

# Get the value of N for the list to be created
def getListSize():
	not_int = True
	listSize = input('Please enter an integer for the size of the list \n')
	while(not_int):
	     try:
	     	if(type(int(listSize)) is int):
	     		not_int = False
	     		print('Proceeding with the program ')
	     except:
	     	print('The input you entered:', listSize, 'is not an int')
	     	listSize = input('Please enter an integer for the size of the list \n')
	return listSize

def populateList(listSize):
	randNumbers = [] 
	# Populate randNumbers with random numbers 0-10000
	while(listSize != 0):
		randNumbers.append(random.randrange(0, 10000))
		listSize = listSize - 1

	# Print the currentNumbers
	print("Random Numbers in list:")
	for i in range(len(randNumbers)):
		if((i != 0 ) & ((i+1)%10 != 0)):
			print('{0:4d}'.format(randNumbers[i]),' ', end='')
		elif((i != 0 ) & ((i+1)%10 == 0)):
			print('{0:4d}'.format(randNumbers[i]),' ')
		else:
			print('{0:4d}'.format(randNumbers[i]),' ', end='')
	return randNumbers

# sequential search for max number in list
def findValue(randNumbers, prod):

	if(prod == 'min'):
		curValue = 10001
		for i in range(len(randNumbers)):
			if(randNumbers[i] < curValue):
				curValue = randNumbers[i]
	if(prod == 'max'):
		curValue = -1
		for i in range(len(randNumbers)):
			if(randNumbers[i] > curValue):
				curValue = randNumbers[i]
	return curValue


def main():
	listSize = int(getListSize())
	randNumbers = populateList(listSize)
	minInt = findValue(randNumbers, 'min')
	maxInt = findValue(randNumbers, 'max')

	print('Min:',minInt,'Max:',maxInt)
## Start program
main()
	





