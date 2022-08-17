from flask import Flask
app = Flask(__name__)

# Create a root route ("/") that responds with "Hello World"

@app.route('/')
def index():
    return 'Hello World'

# Create a route that responds with "Dojo!"

@app.route('/dojo')
def dojo():
    return 'Dojo'


# Create a route that responds with "Hi" and whatever name is in the URL after /say/

@app.route('/say/<string:name>')
def hi(name):
    print(name)
    return f"Hi {name}" 

#Lisa is cool and Zack too!
# Create one url pattern and function that can handle the following 
# examples (HINT: int() will come in handy! For example int("35") returns 35):

# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
# We hope you are feeling more comfortable with routes now!


@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f' {num * word}'


if __name__ == "__main__":
    app.run(debug=True)