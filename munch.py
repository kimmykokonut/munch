'''
Munch App MVP
v0.1
By Applause
The purpose of Munch is to produce a dinner menu from favorite dishes
and produce a shopping list of ingredients if required.
'''
'''
2.0 by Kim
-updated to print grocery list numbered, alphabetized and removed duplicates
-updated to add while loop to run program again
-updated to allow user to ask for shopping list in case of error answer
-updated to allow user to type Y or y for yes.
'''
#-----Imports----------------------------
from random import choice

# A. functions -------------------------

# a1. chooseDishes
def chooseDishes(days):     #how does days == answer?***
    while len(myMenu) < (days):  
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu...")
    print() #print blank line
    for dish in myMenu:  #to print list vertically without brackets and commas
        print(myMenu.index(dish) + 1, dish) #different way to print numbered list.
    print()
    print("Out of all these dishes, my favorite has to be.. " + choice(myMenu))

    '''
    1. choose rando dish from foodWeLike DONE
    2. make sure dish isn't already chosen, then add to myMenu list DONE
    3. repeat until we have required number of dishes in myMenu DONE
    '''
# a2. shoppingList
def buildShoppingList():
    myShoppingList = []  #created inside function. also ok outside, this is cleaner. this is local in scope, can only print inside function
    if "Lentil Soup" in myMenu:
        myShoppingList.append(lentilSoup)
    if "Thali Bowls" in myMenu:
        myShoppingList.append(thaliBowls)
    if "Baked Potatoes" in myMenu:
        myShoppingList.append(bakedPotatoes)
    if "Japanese Pancakes" in myMenu:
        myShoppingList.append(japanesePancakes)
    if "Pasta Marinara" in myMenu:
        myShoppingList.append(pastaMarinara)
    if "Burritos" in myMenu:
        myShoppingList.append(burritos)
    if "Salad Nicoise" in myMenu:
        myShoppingList.append(saladNicoise)
    print()
    #print(myShoppingList)
    finalShoppingList = []  #--------want to alpha and remove dupes in list. KR
    for dishes in range(len(myShoppingList)):    #Make nested list into 1 list
        for item in range(len(myShoppingList[dishes])):
            #if item not in finalShoppingList:  #takes care of dupes. not working
            finalShoppingList.append(myShoppingList[dishes][item]) #makes 1 list
    finalShoppingList.sort()  #alpha sort.
    for food in finalShoppingList:
        while(finalShoppingList.count(food) > 1) : #checks for repeat item
              finalShoppingList.remove(food)   #removes dupes
    #print(finalShoppingList) #but prints as ugly list
    '''for ingredients in myShoppingList:  #this was in tutorial to print nested list as vertical indiv. words
        for ingredient in ingredients:     
            print(ingredient)'''
    #for ingredient in finalShoppingList: #prints list as vertical w/o [] and "" and ,
        #print(ingredient)
    counter = 1             #prints list vertical using counter variable, numbered
    for item in finalShoppingList:
        output = f'{counter}. {item}'
        print(output)
        counter += 1
    print()
    print('Voila! Bon appetit')

#a.3 new function for sign off
def sign_off():
    print()
    print("No worries. Buon appetito!")
            
# B. lists -------------------------------

# b1. list of favorite meals
foodWeLike = ["Lentil Soup", "Thali Bowls", "Baked Potatoes", "Japanese Pancakes", "Pasta Marinara", "Burritos", "Salad Nicoise"]
#print(foodWeLike)

myMenu = [] #blank to autopopulate with chooseDishes function GLOBAL in scope

#myShoppingList = []  *Moved into function to make local scope. more modulear

# b2. list of ingredients per meal
#dish = ['ing1', 'ing2'] #advanced, turn into 2D lists to link meal w ing, but then dishes become varianble adn can't have spaces

lentilSoup = ['Lentils', 'Onions', 'Garlic', 'Carrots', 'Zucchini', 'Spinach', 'Diced Tomatoes', 'Frozen Corn']
thaliBowls = ['Brown Rice', 'Black Beans', 'Salsa', 'Cheddar Cheese', 'Black Olives', 'Sour Cream', 'Avocado', 'Cilantro', 'Thali Sauce']
bakedPotatoes = ['Russet Potatoes', 'Sour Cream', 'Cheddar Cheese', 'Soy Curls', 'Spinach', 'Black Olives']
japanesePancakes = ['Eggs', 'Cilantro', 'Onion', 'Cabbage', 'Flour', 'Mayonaise', 'Sriracha', 'Soy Sauce', 'Sesame Oil', 'Kale', 'Carrots']
pastaMarinara = ['Pasta', 'Tomato Sauce', 'Cheese', 'Chickpeas', 'Kale']
burritos = ['Tortillas', 'Beans', 'Rice', 'Cheese', 'Salsa', 'Sour Cream', 'Avocado', 'Cilantro', 'Olives']
saladNicoise = ['Eggs', 'Green Beans', 'Chickpeas', 'Olives', 'Lettuce', 'Nicoise Dressing', 'Potatoes', 'Shallot', 'Cherry tomatoes']

#1. How many days to plan?
again = "y"
while again == "y":
    print("Hello, I'm Munch! I'll help you to plan your dinner menu...")
    answer = input("How many days would you like me to plan?  ") #stored as string. but if choose >7, program does nothing
    answer = int(answer) #otherwise can't get function outliers of 0 or >7 

    if answer < 1 or answer > 7:
        print("Error, you must choose between 1 and 7 dishes until we can accomodate more input.") #code in try again?
        again =  input("Try again? 'y' or 'n' ")
        continue
    if again != "y":
        print("Good-Bye")
        break

    print(f"Ok, I'm going to plan {answer} dinner(s) from your favorite meals list.") 

#2. Choose dishes? (function)
    chooseDishes(answer)

#3. Build shopping list (function)

    answer = input("Would you like a shopping list for this menu? Enter 'y' or 'n' ").lower()

    if answer == 'y':
        buildShoppingList() # call build shopping list **Don't need to use print() bc it's its own function
        break
    elif answer != 'y':
        ask_again = input("Double checking you said no? Type 'y' if you want the shopping list: ").lower()
        if ask_again == 'y':
            buildShoppingList()
            break
        else:
            sign_off() #calling sign off function
            #put new function here to make code modular, so can change ending if desired.
            #print("No worries. Buon appetito!")
            break

'''solution idea for step 3: from Applause
while True:
    answer = input("Would you like a shopping list for this menu? Enter 'y' or 'n'...")
    if answer in  ('y', 'Y', 'n', 'N'):
        break
    print("Hmm, didn't catch that. Try again.")

if answer in ('y', 'Y'):
    buildShoppingList()
else:
    print()
    print("You got it! Bye for now.")
    '''