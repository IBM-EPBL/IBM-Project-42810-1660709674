from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
     return 'home page'
@app.route('/about')
def home():
     return 'about page'
@app.route('/signup')
def signup():
     return 'signup'
@app.route('/signin')
def signin():
     return 'signin page'
if __name__ == '__main__':
     app.run(debug=True)
