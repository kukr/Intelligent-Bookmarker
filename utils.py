import requests # Import the requests library to make HTTP requests
from bs4 import BeautifulSoup # Import BeautifulSoup for HTML parsing
from gensim.parsing.preprocessing import preprocess_string # Import preprocess_string function from gensim library

# Send an HTTP GET request to the specified URL
# Parse the HTML content using BeautifulSoup
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract text from various HTML elements
    elements = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "span", "strong", "em", "a"])
    # Find all HTML elements specified in the list and store them in the 'elements' variable
    content = " ".join([elem.get_text() for elem in elements])
    return content # Return the extracted text content

# Call the preprocess_string function from the gensim library to preprocess the input string
# with no specified filters and return the preprocessed string
def preprocess_string(s):
    return preprocess_string(s, filters=None)