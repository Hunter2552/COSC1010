#
# Hunter Richardson
# 10/21/2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 



#read and define filename, I did this because it wasn't reading "numbers.txt"
def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = file.readlines()
        
        # Convert each line to an integer
        numbers = [int(num.strip()) for num in numbers]
        
        # Calculate the average
        average = sum(numbers) / len(numbers)
        
        return average
    #troubleshoot code for file not found, (I did this because file not found kept coming up)
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "File contains non-integer values."
    except ZeroDivisionError:
        return "File is empty."

# Definitions
filename = 'numbers.txt'
average = calculate_average(filename)
print(f"The average is: {average}")