#
# Hunter richardson
# 12/4/2024
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def to_pig_latin(word):
    # Convert the word to Pig Latin
    return word[1:] + word[0].lower() + "ay"


def main():
    # Sentence from the user
    sentence = input("Enter a sentence: ")
    


    # Split the sentence into words
    words = sentence.split()
    
    # Convert func.
    pig_latin_words = [to_pig_latin(word) for word in words]
    
    # words->sentence
    pig_latin_sentence = " ".join(pig_latin_words)
    
    # Print pig Latin
    print("Pig Latin:", pig_latin_sentence)



# Call the MAIN
main()
