# Flask Language Translation App

A web-based language translation application built with Flask.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/RepoRange/Translate.ai

```

```
cd Translate.ai

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

## Project Structure

```
Translate.ai/
│
├── assets/          # Static assets directory
│   ├── images/      # Images for web pages
│   └── css/         # CSS stylesheets
│
├── templates/       # HTML templates
├── app.py          # Main application file
├── .env            # Environment variables
└── requirements.txt # Project dependencies
```

## Asset Guidelines

- Supported image formats: PNG, JPG, SVG
- Maximum image size: 5MB
- Recommended image dimensions:
  - Logos: 200x200px
  - Banners: 1200x300px
  - Icons: 32x32px

## API Endpoints

- `GET /`: Home page
- `POST /translate`: Translation endpoint
