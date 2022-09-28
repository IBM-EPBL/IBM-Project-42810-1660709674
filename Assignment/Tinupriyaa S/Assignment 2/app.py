from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
     return 'hello'
@app.route('/about')
def about():
     return 'know about this page'
@app.route('/signup')
def signup():
     return 'signup'
@app.route('/signin')
def signup():
     return 'login'
if __name__ == '__main__':
     app.run(debug=True)
