from flask import Blueprint, jsonify, request
from neo4j import GraphDatabase

recipe_api = Blueprint('recipe_api', __name__)

uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

def execute_query(query, **params):
    with driver.session() as session:
        result = session.run(query, **params) 
        return result

@recipe_api.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()
    recipe_name = data.get('name')
    ingredients = data.get('ingredients')

    # Create recipe node
    query = "MERGE (r:Recipe {name: $recipe_name})"
    execute_query(query, recipe_name=recipe_name)

    # Connect ingredients to recipe
    for ingredient in ingredients:
        query = """
        MERGE (i:Ingredient {name: $ingredient})
        WITH i
        MATCH (r:Recipe {name: $recipe_name})
        MERGE (r)-[:CONTAINS_INGREDIENT]->(i)
        """
        execute_query(query, recipe_name=recipe_name, ingredient=ingredient)

    return jsonify({'message': 'Recipe added successfully'}), 201

@recipe_api.route('/recipes', methods=['GET'])
def get_all_recipes():
    recipes = []
    # Fetch all recipes and ingredients
    with driver.session() as session:
        query = """
        MATCH (r:Recipe)-[:CONTAINS_INGREDIENT]->(i:Ingredient)
        RETURN r.name AS recipe, COLLECT(i.name) AS ingredients
        """
        result = session.run(query)
        for record in result:
            recipes.append({"recipe": record["recipe"], "ingredients": record["ingredients"]})

    return jsonify({'recipes': recipes}), 200

@recipe_api.route('/recipes/<recipe_name>', methods=['DELETE'])
def delete_recipe(recipe_name):
    # Delete recipe implementation
    query = "MATCH (r:Recipe {name: $recipe_name}) DETACH DELETE r"
    execute_query(query, recipe_name=recipe_name)
    return jsonify({'message': 'Recipe deleted successfully'}), 200

