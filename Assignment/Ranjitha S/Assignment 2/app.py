from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
     return 'Welcome'
@app.route('/about')
def about():
     return 'lets know about our page'
@app.route('/signup')
def signup():
     return 'Create Account'
@app.route('/signin')
def signup():
     return 'signin'
if __name__ == '__main__':
     app.run(debug=True)
