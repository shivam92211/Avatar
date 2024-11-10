import subprocess
import sys
import streamlit as st
import PyPDF2
import docx
import re
import spacy
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Function to load spaCy model
def load_spacy_model():
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        # Download model if not present
        print("Downloading en_core_web_sm model for spaCy...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl"])
        nlp = spacy.load("en_core_web_sm")
    return nlp

# Initialize spaCy model
nlp = load_spacy_model()

# Define additional functions for text extraction, NER, sentiment analysis, etc.
def extract_pdf_text(file_path):
    text = ""
    reader = PyPDF2.PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_docx_text(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_file(file):
    if file.name.endswith('.pdf'):
        return extract_pdf_text(file)
    elif file.name.endswith('.docx'):
        return extract_docx_text(file)
    else:
        return "Unsupported file format. Please upload a PDF or DOCX file."

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s.]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

# Named Entity Recognition (NER)
def perform_ner(text):
    doc = nlp(text)
    entities = {
        'characters': set(),
        'locations': set(),
        'dates': set(),
        'organizations': set()
    }
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities['characters'].add(ent.text)
        elif ent.label_ == "GPE":
            entities['locations'].add(ent.text)
        elif ent.label_ == "DATE":
            entities['dates'].add(ent.text)
        elif ent.label_ == "ORG":
            entities['organizations'].add(ent.text)
    return entities

# Sentence Simplification, Summarization, Theme Extraction, Sentiment Analysis functions remain unchanged

# Streamlit App Layout
st.title("Text Analysis Tool")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        raw_text = extract_text_from_file(uploaded_file)
    
    if isinstance(raw_text, str):
        st.subheader("Extracted Text")
        st.write(raw_text[:1000])  # Display the first 1000 characters
        
        # Clean the text
        cleaned_text = clean_text(raw_text)

        # Perform NER
        if st.checkbox("Show Named Entities"):
            entities = perform_ner(cleaned_text)
            st.write("Characters:", entities['characters'])
            st.write("Locations:", entities['locations'])
            st.write("Dates:", entities['dates'])
            st.write("Organizations:", entities['organizations'])

        # Simplify Sentences, Summarize Text, Extract Themes, Sentiment Analysis remain unchanged
    else:
        st.error("Error extracting text. Please upload a valid PDF or DOCX file.")
else:
    st.info("Upload a file to start analysis.")
