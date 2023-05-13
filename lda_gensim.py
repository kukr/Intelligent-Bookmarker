# Import gensim downloader module, Dictionary and TfidfModel from gensim.corpora module and extract_text_from_url, preprocess_string functions from utils.py
import gensim.downloader as api
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from utils import extract_text_from_url, preprocess_string

class GensimLDAClassifier:
    def __init__(self):
        # Load the pre-trained LDA model from gensim's downloader
        self.lda_model = api.load("lda-wiki-100")

        # Load the dictionary used for the LDA model
        self.dictionary = Dictionary.load("static/lda_wiki_100_dictionary.dict")

        # Load the TF-IDF model used for the LDA model
        self.tfidf_model = TfidfModel.load("static/lda_wiki_100_tfidf_model.tfidf")

    def categorize_website(self, url):

        # Extract text content from the given URL
        content = extract_text_from_url(url)

        # Preprocess the text by applying some filters and tokenizing it
        tokens = preprocess_string(content)

        # Convert the preprocessed text into a bag-of-words representation
        bow = self.dictionary.doc2bow(tokens)

        # Apply TF-IDF transformation to the bag-of-words representation
        tfidf = self.tfidf_model[bow]

        # Get the topic probabilities for the document
        topic_probabilities = self.lda_model.get_document_topics(tfidf, minimum_probability=0)

        # Get the index of the topic with the highest probability
        topic_idx = max(topic_probabilities, key=lambda x: x[1])[0]

        # Get the top n words for the topic with the highest probability
        topic_label = self.lda_model.print_topic(topic_idx, topn=3)
        return topic_label