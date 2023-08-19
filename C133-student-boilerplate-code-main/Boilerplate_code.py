from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', message='Welcome to Alex\'s Family Tree!')

@app.route('/family')
def family():
    family_members = [
        {
            "name": "John",
            "age": 35,
            "picture": "john.jpg"
        },
        {
            "name": "Mary",
            "age": 33,
            "picture": "mary.jpg"
        },
        {
            "name": "Alex",
            "age": 8,
            "picture": "alex.jpg"
        }
    ]
    return render_template('family.html', family_members=family_members)

if __name__ == '__main__':
    app.run(debug=True)