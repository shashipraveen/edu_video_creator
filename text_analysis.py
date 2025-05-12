import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

# Download necessary NLTK data (only once)
nltk.download('punkt')
nltk.download('stopwords')


def analyze_text(text):
    """
    Analyze the educational input text and split it into structured content.
    Returns a dictionary with title and list of slide contents.
    """
    # Step 1: Clean and tokenize
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    
    # Step 2: Generate slide headings (basic heuristic: 1 slide per 2 sentences)
    slides = []
    for i in range(0, len(sentences), 2):
        chunk = " ".join(sentences[i:i+2])
        words = word_tokenize(chunk)
        keywords = [word for word in words if word.lower() not in stop_words and word not in string.punctuation]
        heading = " ".join(keywords[:3]) + "..." if keywords else "Topic"
        slides.append({"heading": heading, "content": chunk})

    return {
        "title": "Auto-Generated Lesson",
        "slides": slides
    }
