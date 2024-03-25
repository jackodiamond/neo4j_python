from flask import Blueprint, jsonify, request
from recipe import execute_query

ingredient_api = Blueprint('ingredient_api', __name__)

    
@ingredient_api.route('/recipes/ingredients/<recipe_name>', methods=['PUT'])
def change_recipe_ingredients(recipe_name):
    data = request.get_json()
    new_ingredients = data.get('ingredients')

    # Delete existing ingredients
    query = "MATCH (r:Recipe {name: $recipe_name})-[rel:CONTAINS_INGREDIENT]->(i) DELETE rel"
    execute_query(query, recipe_name=recipe_name)

    # Add new ingredients
    for ingredient in new_ingredients:
        query = """
        MERGE (i:Ingredient {name: $ingredient})
        WITH i
        MATCH (r:Recipe {name: $recipe_name})
        MERGE (r)-[:CONTAINS_INGREDIENT]->(i)
        """
        execute_query(query, recipe_name=recipe_name, ingredient=ingredient)

    return jsonify({'message': 'Ingredients changed successfully'}), 200
