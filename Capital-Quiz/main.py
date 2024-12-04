#
# Name
# Date
# Capital Quiz Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

import random

def main():
    # Initialize the dictionary of U.S. states and capitals
    capitals = {
        'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
        'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
        'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
        'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
        'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
        'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
        'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
        'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
        'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
        'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

    # Initialize score counters
    correct_answers = 0
    incorrect_answers = 0

    # Main loop
    while True:
        # Randomly select a state from the dictionary
        state = random.choice(list(capitals.keys()))
        
        # Questioneee
        user_answer = input(f"What is the capital of {state}? (Type 'quit' to exit): ").strip()

        # Quiter or not
        if user_answer.lower() == 'quit':
            break
        
        # Answer
        correct_capital = capitals[state]
        if user_answer.lower() == correct_capital.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is {correct_capital}.")
            incorrect_answers += 1

    # Display the final score
    print("\nGame Over!")
    print(f"Correct answers: {correct_answers}")
    print(f"Incorrect answers: {incorrect_answers}")

# Call the main function to start the quiz
main()

