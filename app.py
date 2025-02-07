from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def get_digit_sum(n):
    """Calculate the sum of a number's digits."""
    return sum(int(digit) for digit in str(n))

def get_fun_fact(n):
    """Fetch a fun fact about the number from the Numbers API."""
    response = requests.get(f"http://numbersapi.com/{n}/math?json")
    if response.status_code == 200:
        return response.json().get("text", "No fun fact found.")
    return "Could not retrieve a fun fact."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """API endpoint to classify a given number."""
    number = request.args.get('number')

    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []

    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": get_digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
