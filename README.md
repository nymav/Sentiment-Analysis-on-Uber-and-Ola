# Sentiment Analysis on Uber and Ola

This project analyzes public sentiment around Uber and Ola services using Twitter data. It leverages deep learning models like CNNs and MLPs to classify tweets into positive or negative sentiment. A Flask-based web interface allows users to interact with the trained model and make predictions.

## Overview

- **Data**: 3000 tweets about Uber and Ola (CSV format)
- **Tech Stack**: Python, Flask, Scikit-learn, TensorFlow, Word2Vec, SQLite
- **Models Used**:
  - Convolutional Neural Networks (CNN)
  - Multi-layer Perceptron (MLP)
- **UI**: Basic user registration, login, and input-based sentiment prediction

## Project Structure

```bash
 model.ipynb        # Jupyter Notebook with model training and visualizations
 app.py             # Flask web app backend
 model.pkl          # Trained ML model
 cv.pkl             # CountVectorizer/TF-IDF model
 signup.db          # SQLite database for login/signup
 Uber_3000.csv      # Dataset: Tweets about Uber
 Ola_3000.csv       # Dataset: Tweets about Ola
```

## Features

- Tweet preprocessing (removal of stop words, hyperlinks, etc.)
- Sentiment classification using deep learning
- Flask-based web app with:
  - User signup/login
  - Input field for tweet text
  - Real-time prediction
- Cleaned and stored models (`model.pkl`, `cv.pkl`) for reuse

## How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

## Ignored Files

Make sure the following files are not committed (via `.gitignore`):

```
Notebook.ipynb
*.db
__pycache__/
*.pkl
.ipynb_checkpoints/
```

## Future Improvements

- Expand to multi-class sentiment (e.g., neutral, sarcastic)
- Use pre-trained transformer models like BERT
- Enhance UI with modern frontend frameworks (React, Vue)
- Integrate live Twitter scraping with Tweepy

## Authors

Nikhil Y

## License

This project is licensed for academic use only.
