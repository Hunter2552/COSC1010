#
# Hunter Richardson
# 9/23/2024
# Bug Collector Programming Project
# COSC 2409 DNT
#
# Initialize variables for bugs and total number of bugs collected.

# Get number of bugs collected each day using a for loop.

# Display the total number of bugs collected.

#initialize the accumulator
total=0

# Get the bugs collected for each day
for day in range (1, 8):
    # Prompt the user
    print('Enter bugs collected on day', day)

    # Input the number of bugs
    bugs = int(input())

    # Add bugs to total
    total+=bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.' )