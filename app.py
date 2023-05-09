from flask import Flask, request, jsonify
from flask_cors import CORS
#from lda_api import categorize_website
from openai_classification import categorize_website

app = Flask(__name__)
CORS(app)

@app.route('/categorize', methods=['POST'])
def categorize():
    #print("Reached here")
    url = request.json['url']
    print(url)
    category = categorize_website(url)
    #print(category)
    return jsonify({"category": category})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
