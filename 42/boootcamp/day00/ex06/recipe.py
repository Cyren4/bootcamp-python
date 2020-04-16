
cookbook = { 'sandwich' : (["ham", "bread", "cheese", "cheese", "tomatoes"], 'lunch', 10)\
		,'cake' : (['flour', 'sugar', 'eggs'], 'dessert', 60)
		,'salad': (['avocado', 'arugula', 'tomatoes', 'spinch'], 'lunch', 15)
	}

#add
#print keys
def	show_recipe_name():
	for i in cookbook:
		print(i)

'''
#print values
for i in cookbook:
	print(cookbook[i])

#print all
print cookbook'''

# 2.
def	show_recipe(recipe_name):
	print("Recipe for %s:" %(recipe_name))
	ingredients, meal, prep_time = cookbook[recipe_name]
	print (f'Ingredients list: {ingredients}')
	print ("To be eaten for %s" %(meal))
	print ("Take %d minutes of cooking" %(prep_time))

# 3.

def	del_recipe(recipe_name):
	if recipe_name in cookbook:
		del cookbook[recipe_name]

# 4.

def	add_recipe(recipe_name, ingredients, meal, prep_time):
	cookbook[recipe_name] = (ingredients, meal, prep_time)

# 5.

def	show_all_recipe():
	for i in cookbook:
		show_recipe(i)	
		print ("\n")
	
# 6
print ("Please select an option by typing the corresponding number:\n")
print ("1. Add a recipe")
print ("2. Delete a recipe")
print ("3. Print a recipe")
print ("4. Print the cookbook")
print ("5. Quit")
i = int(input())
print ("\n")
while not(i <= 5 and i > 0):
	print ("This option does not exist, please type the corresponding number.")
	print ("To exit, enter 5.")
	i = int(input())
if i == 1:
	print ("\nWhat is the recipe name?")
	name = input()
	print ("What are the ingredients?")
	ingredients = input().split(',')
	print ("During which meal do you eat it?")
	meal = input()
	print ("How long does it take to cook it?")
	prep_time = int(input())
	add_recipe(name, ingredients, meal, prep_time)
	show_all_recipe()
	
if i == 2:
	print ("\nPlease enter the recipe's name to delete it:")
	show_recipe_name()
	recipe_name = input()
	while recipe_name not in cookbook:
		print ("This recipe is not available.\nTry another one.\nTo exit enter 5.")
		recipe_name = input()
		if recipe_name == 5:
			exit()
	del_recipe(recipe_name)
	print("\n%s had been deleted\n" %(recipe_name))
	print ("The cookbook has now:")
	show_recipe_name()
if i == 3:
	print ("\nPlease enter the recipe's name to get its details:")
	show_recipe_name()
	recipe_name = input()
	while recipe_name not in cookbook:
		print("This recipe is not available.\nTry another one.\nTo exit enter 5.")
		recipe_name = input()
		if recipe_name == 5:
			exit()
	show_recipe(recipe_name)
if i == 4:
	show_all_recipe()
if i == 5:
	print ("Cookbook closed")
	exit()
