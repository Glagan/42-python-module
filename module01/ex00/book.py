from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name: str) -> None:
        try:
            if not isinstance(name, str) or not name:
                raise TypeError(
                    'Invalid name {}. Must be a string.'.format(name))
            self.name = name
        except TypeError as err:
            print(err)
            exit()
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name: str) -> None:
        """
        Print a recipe with the name `name` and returns the instance
        """
        if not isinstance(name, str) or not name:
            raise TypeError(
                '{} is not a valid recipe Name. Must be a non empty string.'.format(name))
        found = False
        for k, v in self.recipes_list.items():
            for recipe in v:
                if recipe.name == name:
                    print(str(recipe))
                    found = True
                    break
            if found:
                break
        if not found:
            print('No recipe with the name {} yet.'.format(name))

    def get_recipes_by_types(self, recipe_type: str) -> list:
        """
        Get all recipe names for a given recipe_type
        """
        if recipe_type not in ['starter', 'lunch', 'dessert']:
            raise TypeError('recipe_type must be starter, lunch or dessert.')
        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe: Recipe) -> None:
        """
        Add a recipe to the book and update last_update
        """
        if not isinstance(recipe, Recipe):
            raise TypeError('{} is not a Recipe'.format(recipe))
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
