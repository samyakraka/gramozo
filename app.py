from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Initialize Gemini API client
API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

# System prompts for different functionalities
GRAMMAR_CORRECTION_PROMPT = """You are a professional grammar correction assistant. Your task is to correct grammar, spelling, punctuation, and syntax errors in the provided text while maintaining the original meaning and tone. 

IMPORTANT RULES:
- Do not use asterisks (*) or any markdown formatting in your response
- Do not add bold, italic, or any special formatting
- Return only the corrected text without any explanations or additional commentary
- Preserve the original structure and style of the text
- Make minimal changes necessary to fix errors

Text to correct:"""

HUMANIZATION_PROMPT = """You are an AI content humanization specialist. Your task is to rewrite AI-generated content to make it sound more natural, conversational, and human-like while maintaining the core message and information.

IMPORTANT RULES:
- Do not use asterisks (*) or any markdown formatting in your response
- Do not add bold, italic, or any special formatting
- Return only the humanized text without any explanations or additional commentary
- Make the text sound natural and conversational
- Add human-like expressions, varied sentence structures, and natural flow
- Maintain the original meaning and key information

Text to humanize:"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        operation = data.get('operation', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Choose the appropriate prompt based on operation
        if operation == 'grammar':
            prompt = GRAMMAR_CORRECTION_PROMPT + "\n\n" + text
        elif operation == 'humanize':
            prompt = HUMANIZATION_PROMPT + "\n\n" + text
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        # Generate content using Gemini API
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        
        return jsonify({'result': response.text})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# This block is only for local development
# In production (Vercel), the app object will be imported directly
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6000))
    app.run(host='0.0.0.0', port=port, debug=False)
