#
# Hunter Richardson
# 12/2/2024
# Vowels and Consonants Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
#definition
def num_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    v_count = 0
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1
    return v_count
#definition
def num_consonants(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    c_count = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1
    return c_count
#Main Function
def main():
    # Get a string from the user
    user_str = input('Enter a string of characters: ')
    
    # Report the vowels and consonants
    print('That string has', num_vowels(user_str), 'vowels and', 
          num_consonants(user_str), 'consonants.')

# Call main function
main()
