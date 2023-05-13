# Import the Flask, request and jsonify from the flask module, flask_cors from the flask_cors module, openai_classification from the categorize_website module
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai_classification import categorize_website

# Create an instance of the Flask class
app = Flask(__name__)
# Enable CORS for the Flask app
CORS(app)

# Create a route decorator to tell Flask what URL should trigger the function
@app.route('/categorize', methods=['POST'])
def categorize():
    # Get the URL from the JSON data in the request
    url = request.json['url']
    print(url)

    # Call the categorize_website function to get the category for the URL
    category = categorize_website(url)

    # Return the category as JSON response
    return jsonify({"category": category})

# Run the Flask app on default port 5000
if __name__ == '__main__':
    app.run(debug=True, threaded=True)