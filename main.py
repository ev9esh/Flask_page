from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nulllable=False)
    intro = db.Column(db.String(300), nulllable=False)
    text = db.Column(db.Text, nulllable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Article %r' % self.id


@app.route('/')
@app.route('/home')
def index():
    name, age, prof = 'Jack', 29, 'Programmer'
    template_context = dict(name=name, age=age, prof=prof)
    return render_template('index.html', **template_context)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: ' + name + '-' + str(id)


if __name__ == '__main__':
    app.run(debug=True)
