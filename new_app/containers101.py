from flask import Flask
import socket

# Application Object
app = Flask(__name__)

# View functions
@app.route('/')
def index():
    return "Hello makers from {}!".format(socket.gethostname())

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)