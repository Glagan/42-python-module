from book import Book
from recipe import Recipe

# Valid Recipe and the __str__ method
r = Recipe('Fish', 1, 10, ['fish', 'salt', 'pepper'],
           'lunch', description='A very nice fish\nMust be eaten cooked.\nUncooked fish will make you less alive.')
print(r)

# Test all Recipe arguments validation
try:
    bad_recipe = Recipe(123, 1, 10, ['fish', 'salt', 'pepper'], 'lunch')
except BaseException:
    pass

try:
    bad_recipe = Recipe('Test', 0, 10, ['fish', 'salt', 'pepper'], 'lunch')
except BaseException:
    pass

try:
    bad_recipe = Recipe('Test', 6, 10, ['fish', 'salt', 'pepper'], 'lunch')
except BaseException:
    pass

try:
    bad_recipe = Recipe('Test', 3, -123, ['fish', 'salt', 'pepper'], 'lunch')
except BaseException:
    pass

try:
    bad_recipe = Recipe('Test', 3, 10, [], 'lunch')
except BaseException:
    pass

try:
    bad_recipe = Recipe('Test', 3, 10, [123, 'salt', 'pepper'], 'lunch')
except BaseException:
    pass

try:
    bad_recipe = Recipe('Test', 3, 10, ['fish', 'salt', 'pepper'], 'supper')
except BaseException:
    pass

try:
    bad_recipe = Recipe(
        'Test', 3, 10, ['fish', 'salt', 'pepper'], 'dessert', 213)
except BaseException:
    pass

# Valid Book
print('')
book = Book('Python')

# Invalid Book
try:
    bad_book = Book(123)
except BaseException:
    pass

# Check recipes before and after adding one
book.get_recipe_by_name('Fish')
book.add_recipe(r)
book.get_recipe_by_name('Fish')

# Invalid Recipe
try:
    book.add_recipe('recipe')
except BaseException:
    pass

# Recipes by type and invalid type
print(book.get_recipes_by_types('starter'))
print(book.get_recipes_by_types('lunch'))
print(book.get_recipes_by_types('dessert'))
try:
    print(book.get_recipes_by_types('supper'))
except BaseException:
    pass
