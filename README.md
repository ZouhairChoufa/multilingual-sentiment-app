# Multilingual Sentiment Analysis Web App

This project is a simple web application that provides sentiment analysis for text in multiple languages, including English, Arabic, Spanish, Chinese, and more. The backend is built with Flask, and the sentiment analysis is powered by a pre-trained Hugging Face Transformers model.


## Features

* **Web Interface:** A simple, clean UI to enter text and view the sentiment result.
* **Multilingual Support:** Accurately analyzes sentiment for a wide variety of languages, leveraging the `tabularisai/multilingual-sentiment-analysis` model.
* **Real-time Analysis:** Submits text via JavaScript (`fetch`) and returns the classification (e.g., "Positive", "Negative", "Neutral") without a page reload.

## Technology Stack

* **Backend:** Flask
* **Machine Learning:** PyTorch & Hugging Face Transformers
* **Frontend:** HTML, CSS, JavaScript
* **Model:** `tabularisai/multilingual-sentiment-analysis` (a fine-tuned DistilBERT model)

## Project Structure

/ ├── model3_all.py # The main Flask application ├── requirements.txt # Python dependencies ├── static/ # CSS and image files │ ├── homeStyle.css │ ├── style.css │ └── ... (images) ├── templates/ # HTML files │ ├── homePage.html │ └── index.html ├── .gitignore ├── LICENSE └── README.md


## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    python model3_all.py
    ```

5.  **Open your browser:**
    Navigate to `http://127.0.0.1:5000` to see the home page. Click on the "Model" link to go to the analysis page (`http://127.0.0.1:5000/model`).

## How to Use

1.  Open the application in your browser and go to the **Model** page.
2.  Type or paste any text (e.g., "This is a wonderful product!" or "هذا منتج سيء للغاية") into the text area.
3.  Click the "Run Tool" button.
4.  The predicted sentiment will appear in the result box below.