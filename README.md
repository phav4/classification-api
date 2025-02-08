# Number Classification API

This API classifies a given number based on its mathematical properties.

## Endpoint
`GET /api/classify-number?number=<integer>`

### Example Request
GET /api/classify-number?number=371

### Example Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

How to Run Locally
Install dependencies:
```
pip install Flask flask-cors requests
```
Start the server:
```
python app.py
```
Open a browser and visit:
```
http://phav4.pythonanywhere.com/api/classify-number?number=371
```
