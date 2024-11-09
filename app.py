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
from spacy.cli import download
 

# Download the model
download('en_core_web_sm')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Functions for File Text Extraction
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

# Text Cleaning
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

# Sentence Simplification
def simplify_sentence(text):
    doc = nlp(text)
    simplified_sentences = []
    
    for sentence in doc.sents:
        subjects, verbs, objects = [], [], []
        for token in sentence:
            if token.dep_ == 'nsubj':
                subjects.append(token.text)
            elif token.dep_ == 'ROOT':
                verbs.append(token.text)
            elif token.dep_ == 'dobj':
                objects.append(token.text)
        
        if subjects and verbs and objects:
            simplified_sentence = f"{' and '.join(subjects)} {', '.join(verbs)} {' and '.join(objects)}."
            simplified_sentences.append(simplified_sentence)
        else:
            simplified_sentences.append(sentence.text)
    
    return " ".join(simplified_sentences)

# Text Summarization
def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

# Theme Extraction
def extract_themes(text, top_n=9):
    doc = nlp(text)
    keywords = [token.text.lower() for token in doc if token.pos_ == "NOUN" and not token.is_stop]
    keyword_freq = Counter(keywords)
    return [keyword for keyword, _ in keyword_freq.most_common(top_n)]

# Sentiment Analysis
def sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    doc = nlp(text)
    annotated_text = []
    
    for sentence in doc.sents:
        sentiment_score = sia.polarity_scores(sentence.text)['compound']
        if sentiment_score >= 0.05:
            sentiment = "Positive"
        elif sentiment_score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        annotated_text.append((sentence.text, sentiment))
    
    return annotated_text

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

        # Simplify Sentences
        if st.checkbox("Simplify Sentences"):
            simplified_text = simplify_sentence(cleaned_text)
            st.subheader("Simplified Text")
            st.write(simplified_text)

        # Summarize Text
        if st.checkbox("Show Summary"):
            summary = summarize_text(cleaned_text)
            st.subheader("Summary")
            st.write(summary)

        # Extract Themes
        if st.checkbox("Show Themes"):
            themes = extract_themes(cleaned_text)
            st.subheader("Themes")
            st.write(", ".join(themes))

        # Sentiment Analysis
        if st.checkbox("Show Sentiment Analysis"):
            sentiments = sentiment_analysis(cleaned_text)
            st.subheader("Sentiment Analysis")
            for sentence, sentiment in sentiments:
                st.write(f"Sentence: {sentence.strip()} | Sentiment: {sentiment}")
    else:
        st.error("Error extracting text. Please upload a valid PDF or DOCX file.")
else:
    st.info("Upload a file to start analysis.")
