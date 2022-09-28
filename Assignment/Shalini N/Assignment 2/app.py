from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
     return 'hi'
@app.route('/about')
def about():
     return 'about our page'
@app.route('/signup')
def signup():
     return 'sing up'
@app.route('/signin')
def signup():
     return 'signin'
if __name__ == '__main__':
     app.run(debug=True)