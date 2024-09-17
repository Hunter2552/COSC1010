#
# Hunter Richardson
# 9/16/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#
def calculate_packages(Persons_Attending, hot_dogs_per_person):
    total_hot_dogs = Persons_Attending * hot_dogs_per_person

    #Key
    hot_dog_packages = (total_hot_dogs + 9) // 10
    bun_packages = (total_hot_dogs + 7) // 8

    # Leftovers
    leftover_buns = bun_packages * 8 - total_hot_dogs
    leftover_hot_dogs = hot_dog_packages * 10 - total_hot_dogs
    
    return hot_dog_packages, bun_packages, leftover_hot_dogs, leftover_buns

def main():
    Persons_Attending = int(input("Enter the number of Persons attending the cookout: "))
    hot_dogs_per_person = int(input("Enter Hot dogs per person: "))

    hot_dog_packages, bun_packages, leftover_hot_dogs, leftover_buns = calculate_packages(Persons_Attending, hot_dogs_per_person)

    print(f"\nNumber of packages of hot dogs needed: {hot_dog_packages}")
    print(f"Number of packages of hot dog buns needed: {bun_packages}")
    print(f"Leftover hot dogs: {leftover_hot_dogs}")
    print(f"Leftover hot dog buns: {leftover_buns}")

if __name__ == "__main__":
    main()