# Portfolio Chatbot Project

A Flask-based portfolio website with an integrated AI chatbot powered by Groq.

## Features
-   **Portfolio Dashboard**: Resume and project showcase.
-   **AI Chatbot**: Answers questions based on resume data using `llama-3.1-8b-instant`.
-   **Responsive Design**: Mobile-friendly interface.

## Local Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd Portfolio
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    -   Create a `.env` file in the root directory.
    -   Add your Groq API key:
        ```text
        GROQ_API_KEY=your_groq_api_key_here
        ```

4.  **Run the application**:
    ```bash
    python app.py
    ```

## Deployment on Render

1.  Create a new **Web Service** on [Render](https://render.com/).
2.  Connect your GitHub repository.
3.  **Build Command**: `pip install -r requirements.txt`
4.  **Start Command**: `gunicorn app:app`
5.  **Environment Variables**:
    -   Add `GROQ_API_KEY` with your actual API key value.
    -   Add `PYTHON_VERSION` (optional, e.g., `3.11.0`).

## Project Structure
-   `app.py`: Main Flask application.
-   `templates/`: HTML templates.
-   `static/`: CSS, JS, and images.
-   `resume_text_utf8.txt`: Resume data source for the chatbot.
