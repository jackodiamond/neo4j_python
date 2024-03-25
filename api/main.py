from flask import Flask
from recipe import recipe_api
from ingredient import ingredient_api
from user_likes import user_likes_api

app = Flask(__name__)

app.register_blueprint(recipe_api)
app.register_blueprint(ingredient_api)
app.register_blueprint(user_likes_api)

if __name__ == '__main__':
    app.run(debug=True,port=3000)
