from flask import Flask #web server

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world, How do you do?'

@app.route('/whereami')
def whereami():
    return 'I am in Ghana, oh yes! :)'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')