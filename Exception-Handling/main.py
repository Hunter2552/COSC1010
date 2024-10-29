#
# Hunter Richardson
# 10/28/2024
# Exception Handling Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = file.readlines()
        
        # Convert each line to an integer
        numbers = [int(num.strip()) for num in numbers]
        
        # Calculate the average
        average = sum(numbers) / len(numbers)
        
        return average
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "File contains non-integer values."
    except ZeroDivisionError:
        return "File is empty." 
    except IOError: #Added IOE Block
        return "An IOError occurred while accessing the file."

# Definitions
filename = 'numbers.txt'
average = calculate_average(filename)
print(f"The average is: {average}")
