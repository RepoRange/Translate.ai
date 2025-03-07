from flask import Flask, request, render_template, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

app = Flask(__name__)

# Get environment variables
API_URL = os.getenv('GEMINI_API_URL')
API_KEY = os.getenv('GEMINI_API_KEY')

headers = {
    "Content-Type": "application/json"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text", "")
    language = data.get("language", "kn")  # Default to Kannada
    
    prompt = f"""
    Translate this English text into {language}.
    Return ONLY the translation in this exact format:
    **Translation:** "translated_text_here" (*transliteration_if_possible*)

    English: "{text}"
    """
    
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }

    response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(result)
        if "candidates" in result and len(result["candidates"]) > 0:
            translated_text = result["candidates"][0]["content"]["parts"][0]["text"]
            print(translated_text)
            # Extract only the translated text
            try:
                # Extract text between quotes after "Translation:"
                import re
                match = re.search(r'\*\*Translation:\*\*\s*"([^"]+)"', translated_text)
                if match:
                    clean_translation = match.group(1)
                    return jsonify({"translation": clean_translation})
                return jsonify({"translation": translated_text.split('**Translation:**')[-1].strip()})
            except:
                return jsonify({"translation": translated_text})
        else:
            return jsonify({"error": "Unexpected response format"}), 500
    else:
        return jsonify({"error": "Translation API request failed"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
