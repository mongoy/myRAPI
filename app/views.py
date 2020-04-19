import redis
from flask import Flask, request
from flask_restful import Api, Resource
import settings


app = Flask(__name__)
api = Api(app)
# REDIS
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=1)

visit_domains = [
    {
        "domains":
            [
                "ya.ru",
                "funbox.ru",
                "stackoverflow.com"
            ],
        "status": "ok"
    }
]

visit_links = [
    {
        "links":
            [
                "https://ya.ru",
                "https://ya.ru?q=123",
                "funbox.ru",
                "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
            ]
    }
]


# easy web
@app.route('/')
@app.route('/index')
def index():
    return 'Привет Flask!!!'


# RAST web


class HelloFlask(Resource):
    def get(self):
        return {"hello": 'Flask'}


api.add_resource(HelloFlask, '/apiweb')


# +Redis
# qqq = redis.inc

# RASTfull


if __name__ == '__main__':
    app.run(settings.DEBUG)
