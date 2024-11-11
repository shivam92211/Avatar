# AI-Avatar - Text Analysis Tool

[AI-Avatar](https://avatarr.streamlit.app/) is a powerful, user-friendly Streamlit application offering a variety of text analysis tools to enhance understanding and insight into uploaded documents. The app analyzes text from PDF or DOCX files, providing key insights like entity recognition, sentence simplification, summarization, theme extraction, and sentiment analysis.

## Features

- **Named Entity Recognition (NER)**: Identifies entities (people, locations, dates, organizations).
- **Sentence Simplification**: Breaks down complex sentences for easier comprehension.
- **Text Summarization**: Generates concise summaries using the TextRank algorithm.
- **Theme Extraction**: Detects prominent themes and keywords.
- **Sentiment Analysis**: Evaluates the sentiment (positive, negative, neutral) of each sentence.

## Project Structure

```plaintext
project-folder/
├── app.py               # Main code for the Streamlit app
├── requirements.txt     # Required Python libraries
```

### File Descriptions

- **app.py**: Contains the main code to run the text analysis app on Streamlit.
- **requirements.txt**: Lists all dependencies needed to run the app.

## Setup and Deployment

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shivam92211/Avatar.git
   cd Avatar
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

### Deploy on Streamlit Cloud

1. Make sure your project is on a public GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and connect your GitHub.
3. Select the repository and branch for deployment.
4. Streamlit Cloud will automatically:
   - Install required packages from `requirements.txt`.

### Example Usage

1. **Upload** a PDF or DOCX file using the file uploader.
2. Select any of the analysis options:
   - Display Named Entities
   - Simplify Sentences
   - Generate Summary
   - Extract Themes
   - Analyze Sentiment
3. **View Results**: Outputs for each selected analysis will appear directly in the app.

## Requirements

- **Python 3.8+**
- Libraries listed in `requirements.txt`

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
