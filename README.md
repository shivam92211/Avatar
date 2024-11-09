Here’s a `README.md` file tailored for deploying your Streamlit app on Streamlit Cloud. It explains the purpose of each file and how to deploy the app.

---

# Text Analysis Tool

This is a Streamlit app that provides multiple text analysis features, including named entity recognition, sentence simplification, text summarization, theme extraction, and sentiment analysis. The app can process text from uploaded PDF or DOCX files and provides various analytical insights into the content.

## Features

- **Named Entity Recognition (NER)**: Extracts entities such as people, locations, dates, and organizations.
- **Sentence Simplification**: Converts complex sentences into simplified forms.
- **Text Summarization**: Provides a concise summary using the TextRank algorithm.
- **Theme Extraction**: Identifies the most common themes or keywords.
- **Sentiment Analysis**: Analyzes the sentiment of each sentence (positive, negative, or neutral).

## Project Structure

```plaintext
project-folder/
├── app.py               # Main Streamlit app code
├── requirements.txt     # Python dependencies
```

### File Descriptions

- **app.py**: Contains the main Streamlit code for the text analysis tool.
- **requirements.txt**: Lists all Python libraries required to run the app.

## Setup and Deployment

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-analysis-tool.git
   cd text-analysis-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Deploy on Streamlit Cloud

1. Ensure your project is hosted on a public GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and connect your GitHub account.
3. Select the repository and branch for deployment.
4. Streamlit Cloud will automatically:
   - Install Python packages from `requirements.txt`

### Example Usage

1. Upload a PDF or DOCX file using the file uploader in the app.
2. Check or uncheck the available options for each analysis:
   - Show Named Entities
   - Simplify Sentences
   - Show Summary
   - Show Themes
   - Show Sentiment Analysis
3. View the results for each selected analysis option directly in the app.

## Requirements

- **Python 3.8+**
- Packages listed in `requirements.txt`


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This `README.md` provides an overview of the app, setup instructions, and guidance on deploying it to Streamlit Cloud. Adjust the GitHub repository link to match your repository.