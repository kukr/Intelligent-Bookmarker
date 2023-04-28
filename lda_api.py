import json
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

app = Flask(__name__)
CORS(app)

n_topics = 20
n_top_words = 10

# Load dataset
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
X = vectorizer.fit_transform(newsgroups.data)

# Train LDA model
lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
lda.fit(X)

@app.route('/categorize', methods=['POST'])
def categorize():
    content = request.json['content']
    X_new = vectorizer.transform([content])
    topic_distribution = lda.transform(X_new)

    topic_idx = np.argmax(topic_distribution)
    topic_words = lda.components_[topic_idx]
    top_word_indices = topic_words.argsort()[:-n_top_words - 1:-1]
    top_words = [vectorizer.get_feature_names_out()[i] for i in top_word_indices]

    response = {
        'category': f'Topic {topic_idx + 1}',
        'keywords': top_words
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
