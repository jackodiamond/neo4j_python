# data_population.py

from neo4j import GraphDatabase

def populate_data(uri, username, password, recipes):
    driver = GraphDatabase.driver(uri, auth=(username, password))
    session = driver.session()

    for recipe in recipes:
        recipe_name = recipe["name"]
        session.run("MERGE (r:Recipe {name: $name})", name=recipe_name)

        for ingredient_name in recipe["ingredients"]:
            session.run(
                """
                MERGE (i:Ingredient {name: $name})
                WITH i
                MATCH (r:Recipe {name: $recipe_name})
                MERGE (r)-[:CONTAINS_INGREDIENT]->(i)
                """,
                name=ingredient_name,
                recipe_name=recipe_name
            )

    session.close()
    driver.close()
