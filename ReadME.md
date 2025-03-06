# Flask Language Translation App

A web-based language translation application built with Flask.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/RepoRange/Translate.ai
cd language-translation
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- Windows:

```bash
venv\Scripts\activate
```

- Linux/Mac:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory
2. Add your translation API credentials:

```
API_KEY=your_api_key_here
```

## Running the Application

1. Ensure your virtual environment is activated
2. Start the Flask server:

```bash
Python app.py

```

The app will be available at `http://127.0.0.1:5000`

## Project Dependencies

- Flask==2.3.3
- requests==2.31.0
- python-dotenv==1.0.0

## API Endpoints

- `GET /`: Home page
- `POST /translate`: Translation endpoint




