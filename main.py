from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    name, age, prof = 'Jack', 29, 'Programmer'
    template_context = dict(name=name, age=age, prof=prof)
    return render_template('index.html', **template_context)


@app.route('/about')
def about():
    return 'Good by'


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page' + name + '-' + id


if __name__ == '__main__':
    app.run(debug=True)
