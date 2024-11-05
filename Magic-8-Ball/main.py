#
# Hunter Richardson
# 11/4/2024
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the programs

# Import necessary modules
import random
# reed response from file 8ball
def read_responses(file_path):
    """
 #Docstring.... 
    Reads responses from a file and returns them as a list.
    
    Parameters:
    file_path (str): The path to the file containing responses.
#Return list
    Returns:
    List[str]: A list of responses.
    """
    with open(file_path, 'r') as file:
        responses = file.readlines()
    return [response.strip() for response in responses]

def magic_8_ball():
    # Read responses from file (8_Ball_response.txt)
    responses = read_responses('8_ball_responses.txt')
    
    while True:
        # Ask the 8bALL A  question
        question = input("Ask the Magic 8 Ball a yes or no question (or type 'quit' to exit): ")
        
        # Quiet
        if question.lower() == 'quit':
            print("Thanks for playing!")
            break
        
        # 8 ball thinking/response
        print("Thinking... 🎱")
        print(random.choice(responses))
        print()  # Blank line for readability

# Run the Magic 8 Ball program
if __name__ == '__main__':
    magic_8_ball()
