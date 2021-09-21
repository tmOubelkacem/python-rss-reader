from collections import Sequence

from flask import Flask
from flask_restful import Api, Resource
from orjson import orjson

from domain.model.Podcast import Podcast
from domain.service.podcast_reader import list_podcasts

app = Flask(__name__)
api = Api(app)


class Podcasts(Resource):
    def get(self):
        podcasts_by_date: Sequence[Podcast] = list_podcasts()
        # for art in podcasts_by_date:
        # print("> Element : ", orjson.loads(orjson.dumps(art)))
        # pass
        return [orjson.loads(orjson.dumps(art)) for art in podcasts_by_date]


api.add_resource(Podcasts, '/podcasts')

if __name__ == "__main__":
    app.run(port=8081)
