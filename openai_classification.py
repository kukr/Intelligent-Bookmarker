from transformers import pipeline
from transformers import GPT2Tokenizer
from utils import extract_text_from_url
import openai
#from tiktoken.Tokenizer import Tokenizer

openai.api_key = "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"

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

def count_tokens(text):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokens = tokenizer.encode(text)
    return len(tokens)

def tokenize_and_truncate(text, max_tokens=4000):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
    return tokenizer.decode(tokens)

def categorize_website(url):
    #classifier = pipeline("zero-shot-classification", model="sentence-transformers/paraphrase-MiniLM-L6-v2")
    content = extract_text_from_url(url)
    print("Bert reach")

    text = tokenize_and_truncate(content, max_tokens=4000)

    prompt = f"{text}\n\nThis website belongs to the category of (Give me just one word topic label):"
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.3,
      max_tokens=60
    )
    label = response['choices'][0]['text'].strip()
    label = label.replace("This website belongs to the category of:", "").strip()
    print(label)
    return label
