cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    }
}


def print_recipe(recipe: str) -> None:
    if recipe in cookbook:
        print('Recipe for {}:'.format(recipe))
        print('Ingredients list: {}'.format(cookbook[recipe]['ingredients']))
        print('To be eaten for {}.'.format(cookbook[recipe]['meal']))
        print('Takes {} minutes of cooking.'.format(
            cookbook[recipe]['prep_time']))
    else:
        print("This recipe doesn't exist !")


def del_recipe(recipe: str) -> None:
    if recipe in cookbook:
        cookbook.pop(recipe)
        print('Recipe {} deleted.'.format(recipe))
    else:
        print("This recipe doesn't exist !")


def add_recipe(recipe: str, ingredients: list, meal: str, prep_time: int) -> None:
    cookbook[recipe] = {'ingredients': ingredients,
                        'meal': meal,
                        'prep_time': prep_time}


def print_all_recipes() -> None:
    if len(cookbook) == 0:
        print('No recipes in the cookbook !')
    else:
        print('All available recipes:')
        for k in cookbook.keys():
            print('\t{}'.format(k))


def ask_input(query: str) -> str:
    result = str(input(query))
    print('')
    return result


meal_types = ['breakfast', 'lunch', 'dessert', 'diner', 'supper', 'snack']

while True:
    print('Please select an option by typing the corresponding number:')
    print('1: Add a recipe')
    print('2: Delete a recipe')
    print('3: Print a recipe')
    print('4: Print the cookbook')
    print('5: Quit')
    action = ask_input('>> ')
    if action == '5':
        print('Cookbook closed.')
        break
    elif action == '4':
        print_all_recipes()
    elif action == '3':
        recipe = ask_input(
            "Please enter the recipe's name to get its details:\n>> ")
        print_recipe(recipe)
    elif action == '2':
        recipe = ask_input("Please enter the recipe's name to delete:\n>> ")
        del_recipe(recipe)
    elif action == '1':
        # Name
        recipe = False
        while not recipe:
            recipe = ask_input('Recipe name:\n>> ')
            if not recipe:
                print('Your recipe must have a name.\n')
            elif recipe in cookbook:
                print('A recipe with this name already exists.\n')
                recipe = False
        # Ingredients
        print('Recipe Ingredients, one per line, add nothing to finish:')
        ingredients = []
        while not ingredients:
            ingredient = True
            while ingredient:
                ingredient = str(input('>>'))
                if ingredient:
                    ingredients.append(ingredient)
            if not ingredients:
                print('You must add at least one ingredient.')
        print('')
        # Meal
        meal = False
        while not meal:
            meal = ask_input('Type of meal:\n>> ')
            if not meal or meal not in meal_types:
                print("Meal type must be of type {}{}.\n".format(
                    ', '.join(meal_types[::-1]),
                    " or {}".format(meal_types[-1]) if len(meal_types) > 1 else "")
                )
                meal = False
        # Preparation time
        prep_time = False
        while not prep_time:
            prep_time = ask_input('Preparation time in minutes:\n>> ')
            try:
                prep_time = int(prep_time)
                if not prep_time:
                    print('Preparation time must be more than 0.\n')
            except BaseException:
                print('Preparation time must be a number.\n')
                prep_time = False
        # Done
        add_recipe(recipe, ingredients, meal, prep_time)
        print('Recipe {} added to the cookbook !'.format(recipe))
    else:
        print('This option does not exist, please type the corresponding number.')
        print('To exit, enter 5.')
    print('')
