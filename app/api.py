import redis
import settings
from flask_api import FlaskAPI, status
from flask import Flask, url_for, request
# from flask_restful import Api, Resource

app = FlaskAPI(__name__)
# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


# easy web
@app.route('/')
@app.route('/index')
def index():
    return 'Привет Flask!!!'


# RASTfull
@app.route('/api/')
def Flask_API():
    return {'hello': 'FLASK API'}


# RASTfullAPI
# @app.route('/', methods=['GET', 'POST'])
# def visit_list():
#     """
#         List urls
#     """
#     if request.method == 'POST':
#         return {'method': 'POST'}
#     else:
#         return {'method': 'GET'}

@app.route('/api/visited_domains', methods=['GET'])
def visited_domains():
    """
        Print urls visited
    """
    # if 'name' in request.args:
    #     return 'Hello ' + request.args['name']
    #
    # else:
    #     return 'Hello John Doe'
    return 'Hello '# , status.HTTP_200_OK
    # return {'method': 'GET'}


@app.route('/api/visited_links', methods=['POST'])
def visited_links():
    """
        Add urls visited
    """
    if request.method == 'POST':
        return {'method': 'POST'}


if __name__ == '__main__':
    app.run(debug=settings.DEBUG)
