from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    website = '''
<!DOCTYPE html>
<html>
<body>
    <h1>New Webpage </h1>
        <h1><p><a href="/hello_world">Greet the world</a></p><h1>
        <h1><p><a href="/greet">greet a special someone</a></p><h1>
        <h1><p><a href="/celsius_to_fahrenheit">Convert celsius to fahrenheit here</a></p><h1>
        <h1><p><a href="/fahrenheit_to_celsius">Convert fahrenheit to celsius here</a></p><h1>
</body>
</html>'''
    return website


@app.route('/hello_world')
def hello_world():
    return 'Hello World! :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


@app.route('/fahrenheit_to_celsius')
@app.route('/fahrenheit_to_celsius/<f>')
def fahrenheit_to_celsius(f="100"):
    temp_celsius = ((5/9) * float(f)) - 32
    return "fahrenheit is {} and temperature in celsius is {}".format(f, temp_celsius)


@app.route('/celsius_to_fahrenheit')
@app.route('/celsius_to_fahrenheit/<c>')
def celsius_to_fahrenheit(c="100"):
    temp_fahrenheit = ((9/5) * float(c)) + 32
    return "celsius is {} and temperature in fahrenheit is {}".format(c, temp_fahrenheit)

if __name__ == '__main__':
    app.run()
