from flask import Flask,render_template
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/products')
def pro():
    return 'products'




if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, port=8000)