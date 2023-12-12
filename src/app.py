from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


todos = [ { "label": "My first task", "done": False } ]

# specifies the endpoint that will be available to our users
# specifies GET method (for reading data)
@app.route('/todos', methods=['GET'])
# defines a function that will be called by Flask when that endpoint is called by the user
def hello_world():
    return jsonify(todos)
    # defines our function execution and in this case,
    # returns the text "Hello World" to the requesting client or browser


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
# Receive the position that the client wants to delete as the first parameter of the delete_todo endpoint function.
def delete_todo(position):
    print("This is the position to delete: ",position)
    # Remove the task from the list of todos
    todos.pop((position-1))
    
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)