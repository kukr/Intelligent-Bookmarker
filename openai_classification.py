# Import the pipeline, GPT2Tokenizer,  module from the transformers library and openai module, extract_text_from_url function from utils.py
from transformers import pipeline 
from transformers import GPT2Tokenizer
from utils import extract_text_from_url 
import openai 

# Set the OpenAI API key
openai.api_key = "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"

# A list of predefined topics
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

# Create a GPT2Tokenizer object from the GPT2Tokenizer class
# Tokenize the text using the tokenizer
# Return the count of tokens
def count_tokens(text):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokens = tokenizer.encode(text)
    return len(tokens)

def tokenize_and_truncate(text, max_tokens=4000):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
    return tokenizer.decode(tokens)

def categorize_website(url):
    # Extract text content from the given URL
    content = extract_text_from_url(url)
    print("Bert reach")

    # Tokenize and truncate the content to 4000 tokens as the OPENAI API has a limit of 4000 tokens
    text = tokenize_and_truncate(content, max_tokens=4000)

    # Create a prompt by combining the truncated text with a question asking for the category label
    prompt = f"{text}\n\nThis website belongs to the category of (Give me just one word topic label):"
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.3,
      max_tokens=60
    )

    # Use the OpenAI Completion API to generate a response based on the prompt
    # Extract the generated label from the response
    label = response['choices'][0]['text'].strip()
    # Clean up the label by removing the question and the newline character
    label = label.replace("This website belongs to the category of:", "").strip()
    print(label)

    # Return the generated label
    return label