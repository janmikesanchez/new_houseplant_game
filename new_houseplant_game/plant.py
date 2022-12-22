import random

class Plant_Class(): #define class plant that takes 4 attributes
    def __init__(self, plant_dictionary):
        self.info = plant_dictionary
        self.plant_name = plant_dictionary["Plant name"] #string
        self.scientific_name = plant_dictionary["Scientific_name"]
        self.light = plant_dictionary["Light requirements"] #int
        self.water = plant_dictionary["Water requirements"] #int
        self.fertilizer = plant_dictionary["Fertilizer requirements"] #int

    def show_plant_info(self):#method to show the plant info
        
        if self.light == 5: #assigns light score to appropriate string values
            light_score  = "high" #retrieved from dictionary light value. 
        elif self.light == 4:
            light_score = "medium/high"
        elif self.light == 3:
            light_score = "medium"
        elif self.light == 2:
            light_score = "medium/low"
        elif self.light == 1:
            light_score = "low"

        if self.water == 5: #assigns water score to appropriate string values
            water_score  = "high" #retrieved from dictionary water value. 
        elif self.water == 4:
            water_score = "medium/high"
        elif self.water == 3:
            water_score = "medium"
        elif self.water == 2:
            water_score = "medium/low"
        elif self.water == 1:
            water_score = "low"

        if self.fertilizer == 5:#assigns fertilizer score to appropriate string values
            fertilizer_score  = "high" #retrieved from dictionary fertilizer value. 
        elif self.fertilizer == 4:
            fertilizer_score = "medium/high"
        elif self.fertilizer == 3:
            fertilizer_score = "medium"
        elif self.fertilizer == 2:
            fertilizer_score = "medium/low"
        elif self.fertilizer == 1:
            fertilizer_score = "low"

        print(f"-----------------------------------------------\n\nYou have chosen {self.plant_name} {self.scientific_name}\n")
        print(" --------------------Care Label---------------------")
        print(f"The {self.plant_name} {self.scientific_name} needs ")
        print(f"{light_score} light, {water_score} water needs, and")
        print(f"{fertilizer_score} fertilizer requirements.        ")
        print(" ---------------------------------------------------")


    def calculate_score(self, user_light, user_water, user_fertilize):

        #initialize variables in case user over waters. variables are added to final raw score. if user does not over water, 0 will be added, thus not affecting the score. 
        global OVER_WATER, OVER_FERTILIZE, TOO_MUCH_LIGHT, RAW_WATER, RAW_FERTILIZER, RAW_LIGHT, RAW_SCORE, RANDOM_NUM1, RANDOM_NUM2
        OVER_FERTILIZE = 0
        OVER_WATER = 0
        TOO_MUCH_LIGHT = 0
        RANDOM_NUM1 = 0 
        RANDOM_NUM2 = 0#random num 1 and 2 needs to be initialized to be able to be changed for if statement in show_score method. They will remain 0 if RAW_SCORE is >80

        #calculate raw score. should only be out of 100%
        RAW_WATER = ((user_water/(self.water))*100 * 0.6)#water is 60% of plant need 
        if self.water < user_water:
            RAW_WATER = 60 #caps at 60% of raw score
            OVER_WATER = (user_water/self.water)*(-100)*0.05 #if user over waters, score will start subtracting from RAW_SCORE
        RAW_LIGHT = (((user_light/self.light))*100 * 0.3)# light is 30% of plant needs
        if self.light < user_light:
            RAW_LIGHT = 30 #caps at 30% of raw score
            TOO_MUCH_LIGHT = (user_light+self.light)*(-100)*0.025
        RAW_FERTILIZER = (((user_fertilize/self.fertilizer))*100 *0.1)# fertilizer is 10% of plant needs
        if self.fertilizer < user_fertilize:
            RAW_FERTILIZER = 10 #caps at 10 of raw score
            OVER_FERTILIZE = (user_fertilize+self.fertilizer)*(-100)*0.05

        RAW_SCORE =  (RAW_WATER + RAW_LIGHT + RAW_FERTILIZER + OVER_FERTILIZE + OVER_WATER + TOO_MUCH_LIGHT)

       
        

        #assign variable for plant dies to go through while loop in main file
        plant_dies = True

        if RAW_SCORE >=80:
            plant_dies = False
            print(f"Your {self.plant_name} is living and thriving")

        elif RAW_SCORE >= 56 and RAW_SCORE <= 79.99:
            RANDOM_NUM1 = random.randrange(56,80)
            if RANDOM_NUM1 <= 67:
                print("\nYour plant died")
            else:
                plant_dies = False
                print("\nYour plant lives")

        elif RAW_SCORE >= 35 and RAW_SCORE <= 55.99:
            RANDOM_NUM2 = random.randrange(35,56)
            if RANDOM_NUM2<= 50:
                print("\nYour plant died")
            else:
                plant_dies = False
                print("\nYour plant lives!")

        else:
            print("\nYour plant died")

        return plant_dies
        
    def show_score(self, LIGHT, water, fertilize):
        print("\n\n")
        print("light: ", LIGHT) #light score user chose
        print("water: ", water) #water score user input
        print("fertilizer:", fertilize)
        
        print(f"\nraw score: {RAW_SCORE}\nover water score: {OVER_WATER}\nover fertilized score: {OVER_FERTILIZE}\nraw water: {RAW_WATER}\nraw light: {RAW_LIGHT}\nraw fert: {RAW_FERTILIZER}\ntoo much light: {TOO_MUCH_LIGHT}")
   
        print("randon num (raw score 56-80):", RANDOM_NUM1)
    
        print("random num (raw score 35-55):", RANDOM_NUM2)
        