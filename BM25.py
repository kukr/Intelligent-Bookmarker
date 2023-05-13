''' RUN THE FOLLOWING COMMANDS
pip install ntlk gensim rank_bm25
EDIT LINES 18-22. 
LINE 18 CONTAINS THE TARGET WEBSITE
IN LINES 19, 20 ADD WESBITES THAT WERE CATEGORIZED IN THE SAME CATEGORY AS LINE 13 BY THE MODEL UNDER TEST
IN LINES 21, 22 ADD WEBSITES THAT WERE NOT CATEGORIZED IN THE SAME CATEGORY AS LINE 13 BY THE MODEL UNDER TEST
THE CODE WILL GIVE A 4*1 MATRIX RESULT, DENOTING THE SIMILARITY OF LINE 13 WITH EACH OF THE OTHER WEBSITES
HIGHER THE VALUE, HIGHER IS THE SIMILARITY
'''

from nltk.tokenize import word_tokenize
import nltk
from gensim.parsing.preprocessing import STOPWORDS
from rank_bm25 import *
from utils import extract_text_from_url
from nltk.stem import PorterStemmer

url1 = "https://courses.grainger.illinois.edu/cs410/fa2022/"
url2 = "https://courses.grainger.illinois.edu/ece448/sp2023/"
url3 = "https://www.textfixer.com/html/remove-html-tags.php"
url4 = "https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string"
url5 = "https://www.quora.com/What-is-the-purpose-of-A-I"

text1 = extract_text_from_url(url1)
text2 = extract_text_from_url(url2)
text3 = extract_text_from_url(url3)
text4 = extract_text_from_url(url4)
text5 = extract_text_from_url(url5)

words1 = word_tokenize(text1)
words2 = word_tokenize(text2)
words3 = word_tokenize(text3)
words4 = word_tokenize(text4)
words5 = word_tokenize(text5)

all_stopwords_gensim = STOPWORDS
nltk.download('punkt') #REMOVE THIS IF YOU HAVE ALREADY DOWNLOADED OR ADD AN IF CONDITION

def rem_sw(words):
	l = []
	for word in words:
		tokens = word_tokenize(word)
		rem_sw = [t for t in tokens if not t in all_stopwords_gensim]
		s = " ".join(rem_sw)
		l.append(s)
	return l

swrm1 = rem_sw(words1)
swrm2 = rem_sw(words2)
swrm3 = rem_sw(words3)
swrm4 = rem_sw(words4)
swrm5 = rem_sw(words5)

ps = PorterStemmer()

def stem(word):
	return PorterStemmer().stem(word)

stem1 = [stem(w) for w in swrm1]
stem2 = [stem(w) for w in swrm2]
stem3 = [stem(w) for w in swrm3]
stem4 = [stem(w) for w in swrm4]
stem5 = [stem(w) for w in swrm5]

tc = [stem2, stem3, stem4, stem5]
bm = BM25Okapi(tc)
query = stem1
ds = bm.get_scores(query)
print(ds)
