from flask import Flask, render_template,request 

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_todo')
def add_todo():
    item = request.args.get("item")
    return item

@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


