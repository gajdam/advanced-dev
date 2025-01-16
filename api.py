from flask import Flask, jsonify
from flask_restful import Resource, Api

from models.movie import load_movies
from models.link import load_links
from models.rating import load_ratings
from models.tag import load_tags


movies_db = r"db/movies.csv"
links_db = r"db/links.csv"
ratings_db = r"db/ratings.csv"
tags_db = r"db/tags.csv"
app = Flask(__name__)
api = Api(app)


# zad 1
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


# zad 2
class Movies(Resource):
    def get(self):
        movies = load_movies(movies_db)
        return jsonify(movies)


# zad 3
class Links(Resource):
    def get(self):
        links = load_links(links_db)
        return jsonify(links)


class Ratings(Resource):
    def get(self):
        ratings = load_ratings(ratings_db)
        return jsonify(ratings)


class Tags(Resource):
    def get(self):
        tags = load_tags(tags_db)
        return jsonify(tags)


api.add_resource(HelloWorld, "/")
api.add_resource(Movies, "/movies")
api.add_resource(Links, "/links")
api.add_resource(Ratings, "/ratings")
api.add_resource(Tags, "/tags")

if __name__ == "__main__":
    app.run(debug=True)
