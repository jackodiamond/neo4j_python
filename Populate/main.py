# main.py

import data_population

# Example JSON data for recipes and ingredients
recipes = [
    {"name": "Tomato Sauce", "ingredients": ["Tomato", "Onion", "Garlic"]},
    {"name": "Tomato Soup", "ingredients": ["Tomato", "Onion", "Garlic"]},
    {"name": "Classic Grilled Cheese Sandwich", "ingredients": ["Bread", "Cheddar cheese", "Butter"]},
    {"name": "Pasta Aglio e Olio", "ingredients": ["Spaghetti", "Garlic", "Olive oil", "Red pepper flakes", "Parsley"]},
    {"name": "Greek Salad", "ingredients": ["Tomato", "Cucumber", "Red onion", "Feta cheese", "Kalamata olives", "Olive oil", "Red wine vinegar", "Oregano"]},
    {"name": "Pancakes", "ingredients": ["Flour", "Milk", "Egg", "Butter", "Maple syrup"]},
    {"name": "Fruit Salad", "ingredients": ["Apple", "Banana", "Orange", "Strawberry", "Honey", "Lemon juice"]},
    {"name": "Caprese Salad", "ingredients": ["Tomato", "Mozzarella cheese", "Basil", "Balsamic vinegar", "Olive oil"]},
    # Add more recipes as needed
    # Add more recipes as needed
]

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

# Populate data
data_population.populate_data(uri, username, password, recipes)



