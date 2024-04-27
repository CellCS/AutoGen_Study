# filename: keyword_extractor.py

from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from requests import get
import nltk

nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(url):
    # Fetch webpage content
    page = get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Extract text
    text = soup.get_text()

    # Tokenize text (split into list of words)
    words = nltk.word_tokenize(text)

    # Remove non-alphabetic tokens, low-impact words (prepositions, articles, etc.), and one-char tokens
    words = [word for word in words if word.isalpha() 
        and word not in stopwords.words('english') 
        and len(word) > 1]

    # Count frequency of each word (this uses a basic frequency-based approach to keyword extraction)
    counter = Counter(words)
    most_common = counter.most_common(10)  # retrieve top 10 keywords

    print(f"Keywords: {', '.join([word[0] for word in most_common])}")

if __name__ == "__main__":
    extract_keywords('https://www.digihunch.com/2024/03/public-key-infrastructure-3-of-3-use-cases')