from flask import Flask, render_template, request

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            operation_symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            operation_symbol = '-'
        elif operation == 'multiply':
            result = num1 * num2
            operation_symbol = '*'
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
                operation_symbol = '/'
            else:
                return "Error: Cannot divide by zero!"

        return render_template('result.html', num1=num1, num2=num2, operation_symbol=operation_symbol, result=result)

if __name__ == '__main__':
    app.run(debug=True)
