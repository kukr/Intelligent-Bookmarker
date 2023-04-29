import requests
from bs4 import BeautifulSoup
from gensim.parsing.preprocessing import preprocess_string

# def extract_text_from_url(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     paragraphs = soup.find_all("p")
#     content = " ".join([p.get_text() for p in paragraphs])
#     return content

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract text from various HTML elements
    elements = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "span", "strong", "em", "a"])
    
    content = " ".join([elem.get_text() for elem in elements])
    return content


def preprocess_string(s):
    return preprocess_string(s, filters=None)
