import importlib

flask = importlib.import_module('flask')
Flask = flask.Flask
jsonify = flask.jsonify

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return jsonify({'message':'Helloooo Amit'})

    @app.route('/happy')
    def happy():
        return '😊'

    @app.route('/smiley')
    def smiley():
        return ':)'

    return app 