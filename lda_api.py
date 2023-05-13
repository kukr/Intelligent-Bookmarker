# Import the GensimLDAClassifier class from the 'lda_gensim' module
from lda_gensim import GensimLDAClassifier

# Create an instance of the GensimLDAClassifier class
classifier = GensimLDAClassifier()

# Use the classifier to categorize the website based on its content
# Return the generated topic label
def categorize_website(url):
    topic_label = classifier.categorize_website(url)
    return topic_label