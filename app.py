from flask import Flask, abort, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/params', methods=['GET'])
def params():
    data = request.args.get('data', None)
    if data is None:
        abort(418)
    else:
        return 'My data is %s' % data

if __name__ == '__main__':
    app.debug = True
    app.run()
