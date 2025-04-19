#f09ae253
#e88ea5841468997373dbf1c98e2b36a9

#-----------------------NOTES------------------------

# weird API with inconsistent formatting for values within dictionaries/lists
# non-intuitive allergen research - look for free from ingredient instead of just the ingredient or ingredient group
# depending on the ingredient, not all keys are present in the json file - dish type is missing in Matzo Balls



#---------------------Presentation--------------------


# EMILY

# this is what our code does - matches dietary requirements with ingredients from the input, and outputs recipe names, and
# interesting information : cuisine type, dish type, meal type, links and ingredients.
# we worked with for loops and if statements, and created extra functions to optimize the code
# API quirks -
# weird API with inconsistent formatting for values within dictionaries/lists
# non-intuitive allergen research - look for free from ingredient instead of just the ingredient or ingredient group
# depending on the ingredient, not all keys are present in the json file - dish type is missing in Matzo Balls, so if statement to check
# and return only if the key is present in the dictionary


# ANNE
# Our workarounds :
# created a function to remedy the formatting + quick run through of the new function with an if statement for the loopholes and code
# sourced from the internet - using the string module to capitalize each word, "string.capwords(string_diet)", and then join
# " "-".join(string_cap.split()) "
# if statement to check the presence of the key dish type in the dictionary - to not get errors


# PAULA
# enhancements to make it look better with formatting in python - join function, adding delimiters, capitalize letters, colors, text formatting
# next steps - could look into better ingredient classifications so that if you look for nuts or dairy includes all ingredients within that group
# Include calorie information and potentially search for recipes of calories less than a specific number?
# + a downloadable csv spreadsheet with the necessary info -


#Imported request to get http response from the API
#Imported string for string formatting, captilising
import requests
import string
from pprint import pprint

# TEXT COLOR VARIABLES
Red= "\033[31m"
Green= "\033[32m"
Yellow= "\033[33m"
Blue = "\033[34m"
Magenta= "\033[35m"
Cyan= "\033[36m"
End = "\033[0m"

#recipe search function created
#Ingredient is nested into recipe search function
#app id and key have been assigned
#result variable is the get request called
#data is the get request in json format
def recipe_search(ingredient):
    app_id = 'f09ae253'
    app_key = 'e88ea5841468997373dbf1c98e2b36a9'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key)
    )
    data = result.json()
    return data['hits']

# this function formats the input of the user to match the formatting of the values within the JSON file.
# there are a few exceptions - which are outlined in the if else statement

def reformat(string_diet):
    if string_diet == "low sugar" or string_diet == "low potassium" :
        string_cap = string.capwords(string_diet)
        return(string_cap)
    if string_diet == "no oil added" or string_diet == "No oil added":
        string_nw_diet = string_diet.capitalize()
        return(string_nw_diet)
    else :
        string_cap = string.capwords(string_diet)
        return "-".join(string_cap.split())


# example to check if a key is in a dictionary

# def checkKey(my_dict, my_key):
#     if my_key in my_dict.keys():
#         print("here")
#     else:
#         print("Not present")


def run():

    diet_requirement = input(f'Enter your diet : ')
    diet_format = reformat(diet_requirement)
    ingredient = input('Enter an ingredient: ')
    print('-' * 80)
    results = recipe_search(ingredient)

    for result in results:

        recipe = result['recipe']
        if diet_format in recipe["healthLabels"] :

            print (f"This recipe is {diet_format}")
            print(f"{Red}{recipe["label"]}{End}")
            delimiter = "\n"
            print("Cuisine Type: " + str(delimiter.join(recipe["cuisineType"])) + "\n")

            if "dishType" in recipe.keys() :
                print("Dish Type: " + str(delimiter.join(recipe["dishType"])) + "\n")

            print((delimiter.join(recipe["ingredientLines"])) + "\n")
            print("Link to recipe: " + recipe["url"] + "\n")
            print("Meal Type: " + str(delimiter.join(recipe["mealType"])) + "\n")
            print('-' * 80)


run()

