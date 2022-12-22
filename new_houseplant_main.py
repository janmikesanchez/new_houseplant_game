#import plant class
from new_houseplant_game import plant
#assign variables
start_game = True
plant_dictionary = {
"1":{"Plant name": "Pothos", "Scientific_name":"(Epipremnum sp.)", "Light requirements": 2, "Water requirements": 2, "Fertilizer requirements": 1},
"2":{"Plant name": "Cactus", "Scientific_name": "(Mammilaria sp.)", "Light requirements": 5, "Water requirements": 1, "Fertilizer requirements": 1},
"3":{"Plant name": "Peace Lily", "Scientific_name": "(Spathiphyllum sp.)", "Light requirements": 1, "Water requirements": 3, "Fertilizer requirements": 2},
"4":{"Plant name": "African Violet", "Scientific_name": "(Streptocarpus sp.)", "Light requirements": 4, "Water requirements": 3, "Fertilizer requirements": 2},
"5":{"Plant name": "Gardenia", "Scientific_name": "(Rubiaceae sp.)", "Light requirements": 5, "Water requirements": 4, "Fertilizer requirements": 3}
}

def assign_plant(choice): #originally had code for assign_plant in each 1-5 choice
    global PLANT
    PLANT = plant.Plant_Class(plant_dictionary[choice])
    PLANT.show_plant_info()
    return PLANT

input("\n-----------------------------------------------\nHello, welcome to this little houseplant growing game. You \nwill be caring for a plant for 30 days. Every 3rd day, you\nwill select a care task to perform. At the end of the\n30 day period, your plant will live or die (depending on the \ncare you give). Pay attention to the care instructions. Good Luck!\n\n------------ Hit ENTER to continue -------------")

#choose your plant
while start_game == True:
    light = 0
    water = 0.5 #in case user decides not to water, so algorithm is able to #divide by 0
    fertilize = 0.5 
    print("\nYou went to the garden center and decided to pick up your house plant\n")
    while True: #iterate through dictionary values at each "plant name" key in case more are added
        iter = 0
        for name in plant_dictionary.values(): 
            iter += 1
            print(f"{iter}) {name['Plant name']}")
        choice = input("\n\nChoose your plant: ")
        try:
            if int(choice) >= 1 and int(choice) <= len(plant_dictionary):
                assign_plant(choice)
                break
            else:
                print("\n\nNot a valid choice, try again\n\n")
        except ValueError:
            print("\n\nNot a valid choice, try again\n\n")
            

    input("\n------------ Hit ENTER to continue -------------\n")

    #loop to plant placement, will privide light score
    while True:

        choice = input(f"\n\nYou repotted your {PLANT.plant_name}. Now, choose a spot to place your plant:\n 1) Dark corner inside the house\n 2) North facing window\n 3) East/West facing window\n 4) South facing window\n 5) Sunroom/Solarium\n")
        global LIGHT
        if choice == "1":
            LIGHT = int(choice)
            break
        elif choice == "2":
            LIGHT = int(choice)
            break
        elif choice == "3":
            LIGHT = int(choice)
            break
        elif choice == "4":
            LIGHT = int(choice)
            break
        elif choice == "5":
            LIGHT = int(choice)
            break
        else:
            print("\n\nNot a valid choice, try again\n\n")


    #create for loop to iterate through the month and gather user input for water/water+fertilizer
    #this will be every 3rd day for 30 days, gathering input x10 
    for i in range(3,33,3):
        print("------------------------------")
        print(f"Today is day {i} of owning your {PLANT.plant_name} what do you want to do?")
        while True: #while loop to provide choices to perform each for loop iteration
            print("------------------------------")
            care_choice = input("1) Water\n2) Fertilize/water\n3) Do nothing\n  (hit ENTER to do nothing)\n\n")
            if care_choice == "1":
                water = water + 0.5
                break
            if care_choice == "2":
                fertilize = fertilize + 0.5
                water = water + 0.5
                break
            else:
                break



    plant_dies = PLANT.calculate_score(LIGHT, water, fertilize)
    #call on calculate_score method using user input LIGHT, water, and fertilize arguments
    #this returns a boolean value to indicate if the plant lives or dies.
    
    if plant_dies == True:
        print(f"\n\nYour {PLANT.plant_name} care could use some help")


    if plant_dies == True and water > PLANT.water and fertilize > PLANT.fertilizer:
        print(f"It seems like you over watered AND over fertilized your {PLANT.plant_name}")
    elif plant_dies == True and water > PLANT.water:
        print(f"It seems like you over watered your {PLANT.plant_name}")
    elif plant_dies == False and water > PLANT.water:
        print(f"Even though your {PLANT.plant_name} lived, it would have been better with slightly less water.")
    elif plant_dies == True and fertilize > PLANT.fertilizer:
        print(f"It seems like you over fertilized your {PLANT.plant_name}")
    elif fertilize > PLANT.fertilizer:
        print(f"Your {PLANT.plant_name} might have had too much fertilizer")

    if LIGHT > PLANT.light:
        print("It also might have had too much light")
    elif LIGHT < PLANT.light:
        print("It also might not have had enough light")

    while True:
        choice = input("\nWould you like to see your score info? (Y/N)")
        if choice == "y" or choice == "Y":
            PLANT.show_score(LIGHT, water, fertilize)
            break
        else:
            break
    
    while True:
        choice = input("\nWould you like to add a plant to Plant library? (Y/N) ")
        if choice == "y" or choice == "Y":
            #add to plant dictionary by creating new dictionary
            new_dictionary = {"Plant name": "", "Scientific_name": "", "Light requirements": "", "Water requirements": "", "Fertilizer requirements": ""}
            new_dictionary["Plant name"] = input("What is the new plant called?: ")
            new_dictionary["Scientific_name"] = input("What is the scientific name of the new plant: ")
            new_dictionary["Light requirements"] = int(input("How much light does your plant need on a scale from 1-5? (1 being the least amount, and 5 being the most amount): "))
            new_dictionary["Water requirements"] = int(input("How much water does your plant need on a scale from 1-5? (1 being the least amount, and 5 being the most amount): "))
            new_dictionary["Fertilizer requirements"] = int(input("How much fertilizer does your plant need on a scale from 1-5? (1 being the least amount, and 5 being the most amount): "))
            
            plant_dictionary.update({str(len(plant_dictionary)+1): new_dictionary})
            print(f"\n!{new_dictionary['Plant name']} was added to the plant library!\n")
            break
        else:
            break
    replay = input("Would you like to play again? (Y/N) ")
    if replay == "y" or replay == "Y":
        start_game = True
    else: 
        print("Thanks for playing. Goodbye!")
        start_game = False






