class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str, description: str = '') -> None:
        try:
            if not isinstance(name, str) or not name:
                raise TypeError(
                    'Invalid name {}. Must be a string.'.format(name))
            self.name = name
            if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
                raise TypeError(
                    'Invalid Cooking level {}. Must be a number between 1 and 5.'.format(cooking_lvl))
            self.cooking_lvl = cooking_lvl
            if not isinstance(cooking_time, int) or cooking_time < 0:
                raise TypeError(
                    'Invalid Cooking time {}. Must be a number bigger than 0.'.format(cooking_time))
            self.cooking_time = cooking_time
            if not isinstance(ingredients, list) or not ingredients:
                raise TypeError(
                    'Invalid Ingredients {}. Must be a list of strings.'.format(ingredients))
            for ingredient in ingredients:
                if not isinstance(ingredient, str) or not ingredient:
                    raise TypeError(
                        'Invalid Ingredient {}. Must be a non empty string.'.format(ingredient))
            self.ingredients = ingredients
            if not isinstance(recipe_type, str) or recipe_type not in ['starter', 'lunch', 'dessert']:
                raise TypeError(
                    'Invalid Recipe type {}. Must be starter, lunch or dessert.'.format(recipe_type))
            self.recipe_type = recipe_type
            if not isinstance(description, str):
                raise TypeError(
                    'Invalid Description {}. Must be a string.'.format(description))
            self.description = description
        except TypeError as err:
            print(err)
            exit()

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = 'Recipe for {}:\n'.format(self.name)
        txt += '| Cooking level (1-5): {}\n'.format(self.cooking_lvl)
        txt += '| Ingredients list: {}\n'.format(self.ingredients)
        txt += '| To be eaten for {}.\n'.format(self.recipe_type)
        txt += '| Takes {} minutes of cooking.'.format(self.cooking_time)
        if self.description:
            txt += '|| {}\n'.format('\n|| '.join(self.description.split('\n')))
        return txt
