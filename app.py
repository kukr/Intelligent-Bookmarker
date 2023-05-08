# from flask import Flask, request, jsonify
# from lda_api import categorize_website

# app = Flask(__name__)

# @app.route('/categorize', methods=['POST'])
# def categorize():
#     url = request.json['url']
#     category = categorize_website(url)
#     return jsonify({"category": category})

# if __name__ == '__main__':
#     app.run(port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS
#from lda_api import categorize_website
from bert_classification import categorize_website

app = Flask(__name__)
CORS(app)

@app.route('/categorize', methods=['POST'])
def categorize():
    #print("Reached here")
    for i in request.get_json():
        print(i)
    url = request.json['url']
    print(url)
    category = categorize_website(url)
    print(category)
    return jsonify({"category": category})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
