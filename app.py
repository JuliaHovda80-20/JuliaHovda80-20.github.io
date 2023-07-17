from logging.config import dictConfig

from flask import Flask

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

#
# @app.route('/hello',methods=['GET'])
# def hello_world():
#     return 'Hello World!!!!!!!'
#
#
# @app.route('/html', methods=['GET'])
# def html():
#     return render_template('index.html')
#
#
# @app.route('/json', methods=['GET'])
# def json():
#     data = {'message': 'Hello, world!'}
#     return jsonify(data)


from views import *


if __name__ == '__main__':
    app.run(debug=True)


