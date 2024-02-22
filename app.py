from flask import Flask, render_template

app = Flask(__name__)

# Define routes for different arithmetic operations
@app.route('/calc/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return str(result)

@app.route('/calc/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    result = num1 - num2
    return str(result)

@app.route('/calc/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return str(result)

@app.route('/calc/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        return str(result)
    else:
        return "Error: Cannot divide by zero!"

if __name__ == '__main__':
    app.run(debug=True)
