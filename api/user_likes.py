from flask import Blueprint, jsonify, request
from recipe import execute_query

user_likes_api = Blueprint('user_likes_api', __name__)


# API endpoint to add users who liked a recipe
@user_likes_api.route('/recipes/likes/<recipe_name>', methods=['POST'])
def add_likes(recipe_name):
    data = request.get_json()
    users = data.get('users')

    # Create users as separate nodes
    for user in users:
        user_name = user.get('name')
        user_age = user.get('age')
        # Assuming other user details are also provided

        query = """
        MERGE (u:User {name: $user_name, age: $user_age})
        """
        execute_query(query, user_name=user_name, user_age=user_age)

        # Connect user to recipe (assuming the relationship type is LIKES)
        query = """
        MATCH (u:User {name: $user_name}), (r:Recipe {name: $recipe_name})
        MERGE (u)-[:LIKES]->(r)
        """
        execute_query(query, user_name=user_name, recipe_name=recipe_name)

    return jsonify({'message': 'Users who liked the recipe have been added successfully'}), 201
