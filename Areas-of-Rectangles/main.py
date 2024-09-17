#
# Hunter Richardson
# 9/16/2024
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables

# Get length A

# Get width A

# Get length B

# Get width B

# Calculate area A

# Calculate area B

# Print area comparison using if-elif-else statements

# Recatangle 1
Length1=int(input('Length of rectangle 1: '))
Width1=int(input('Width of rectangle 1: '))
# Recatangle 2
Length2=int(input('Length of rectangle 2: '))
Width2=int(input('Width of rectangle 2: '))

#Area
Area1=Length1*Width1
Area2=Length2*Width2

# <,=,> of Area 1 and 2
if Area1>Area2:
    print('Rectangle 1 has a greater area.')
elif Area2 > Area1:
    print('Rectangle 2 has a greater area.')
else:
    print('Both have the same area')
    