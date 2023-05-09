import gensim.downloader as api
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from utils import extract_text_from_url, preprocess_string

class GensimLDAClassifier:
    def __init__(self):
        self.lda_model = api.load("lda-wiki-100")
        self.dictionary = Dictionary.load("static/lda_wiki_100_dictionary.dict")
        self.tfidf_model = TfidfModel.load("static/lda_wiki_100_tfidf_model.tfidf")

    def categorize_website(self, url):
        content = extract_text_from_url(url)
        tokens = preprocess_string(content)
        bow = self.dictionary.doc2bow(tokens)
        tfidf = self.tfidf_model[bow]
        topic_probabilities = self.lda_model.get_document_topics(tfidf, minimum_probability=0)
        topic_idx = max(topic_probabilities, key=lambda x: x[1])[0]
        topic_label = self.lda_model.print_topic(topic_idx, topn=3)
        return topic_label
