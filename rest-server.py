from flask import Flask, jsonify, abort, request, make_response

app = Flask(__name__)

@app.errorhandler(400)
def not_found400(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found404(error):
    return make_response(jsonify( { 'error': 'This is not the service you are looking for' } ), 404)

@app.route('/very/simple/rest/api/v0.1/', methods = ['GET'])
def version():
    return jsonify({'very simple rest api version' : '0.1'} )

@app.route('/very/simple/rest/api/v0.1/do/<command>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def do_something(command):
    #do sth. fancy here
    return jsonify( {'command': command, 'method': request.method, 'args': request.args} )
    
if __name__ == '__main__':
    app.run(debug = True)
