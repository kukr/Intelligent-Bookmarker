from lda_gensim import GensimLDAClassifier

classifier = GensimLDAClassifier()

def categorize_website(url):
    topic_label = classifier.categorize_website(url)
    return topic_label
