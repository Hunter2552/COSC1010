#
# Hunter Richardson
# 10/28/2024
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

import random
MAX_DIGITS=7 # Max number of digit 
START=0  #Start of the random number range
END=9 # End of the random number range

#MainFunc
def main():
    #List
    numbers = [0]*7
    #Populate the list with random numbers.
    for index in range(MAX_DIGITS):
        numbers[index]= random.randint(START, END)
    #Display the random numbers.
    print('Here are your lucky numbers:')
    for index in range(MAX_DIGITS):
        print(numbers[index], end='')
    print() 

 # Call the main back
main()       
