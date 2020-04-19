import json
import redis
import settings
from flask_api import FlaskAPI, status
from flask import Flask, url_for, request, Response

# from flask_restful import Api, Resource

app = FlaskAPI(__name__)
# Connect to our Redis instance
#redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


# easy web
@app.route('/')
@app.route('/index')
def index():
    return 'Привет Flask!!!'


# RASTfull
@app.route('/api/')
def Flask_API():
    return {'hello': 'FLASK API'}


@app.route('/api/visited_domains', methods=['GET'])
def visited_domains():
    """
        Print urls visited
    """
    links = redis.Redis()
    items = []
    count = 0
    for key in links.keys("*"):
        items.append(links.get(key).decode("utf-8"))
        # items.append(str(links.get(key)))
        count += 1
    res_links = ','.join(items)
    if len(items) == 0:
        response = {
            'count': 0,
            'msg': "Found 0 items.",
            'items': "-"
        }
    else:
        response = {
            'count': count,
            'links': f"Found {count} links.",
            'items': res_links
        }
    return response  #, 200, {'Content-Type': 'application/json'}  #Response(response, status=200)
    #return {'method': 'GET'}


@app.route('/api/visited_links', methods=['POST'])
def visited_links():
    """
        Add urls visited
    """
    if request.method == 'POST':
        return {'method': 'POST'}


if __name__ == '__main__':
    app.run(debug=settings.DEBUG)
