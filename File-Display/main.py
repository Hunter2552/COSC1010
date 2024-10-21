#
# Hunter Richardson
# 10/20.2024
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Open the file
# For each line open the file: Read the line, display it, and then close it.

#open the file.
myfile=open('numbers.txt' , 'r')


#Read and displays the file's content.
for line in myfile:
    number=int(line)
    print(number)

#Step 3: Close the file
myfile.close()
