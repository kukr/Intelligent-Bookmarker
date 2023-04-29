from transformers import pipeline
from utils import extract_text_from_url

topics = [
    "Politics",
    "Technology",
    "Sports",
    "Entertainment",
    "Science",
    "Health",
    "Environment",
    "Business",
    "Education",
    "Travel",
    "Food",
    "Fashion",
    "Finance",
    "Art",
    "Automotive",
    "Real Estate",
    "Law",
    "Agriculture",
    "Religion",
    "Pets"
]

def categorize_website(url):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    content = extract_text_from_url(url)
    print("Bert reach")
    result = classifier(content, topics)
    print(result["labels"][0])
    return result["labels"][0]
