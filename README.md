# Gramzo - AI Grammar & Content Assistant 📝✨

A modern, mobile-responsive web application that provides AI-powered grammar correction and content humanization using Google's Gemini API.

## Features

- **Grammar Correction**: Fix grammar, spelling, punctuation, and syntax errors while maintaining the original meaning and tone
- **AI Content Humanization**: Transform AI-generated content to sound more natural, conversational, and human-like
- **Split-Screen Interface**: Clean, intuitive interface with input on the left and output on the right
- **Operation Panel**: Easy-to-use left sidebar for selecting between grammar correction and humanization
- **Modern UI**: Fully responsive design with professional colors and smooth animations
- **Mobile-Friendly**: Optimized for all screen sizes from desktop to mobile

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5 + Custom CSS
- **AI API**: Google Gemini API
- **Icons**: Font Awesome

## Installation & Local Setup

1. **Clone or download this project**

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   - Get your API key from: https://makersuite.google.com/app/apikey

4. **Run the application locally:**

   ```bash
   python app.py
   ```

   The app will start on `http://localhost:6000`

5. **Open your browser and navigate to:**
   ```
   http://localhost:6000
   ```

## Usage

1. **Select Operation**: Choose between "Grammar Correction" or "AI Content Humanization" from the left panel
2. **Enter Text**: Type or paste your text in the input area on the left
3. **Process**: Click the "Process Text" button to generate results
4. **Review & Copy**: View the improved text on the right and copy it to your clipboard

### Grammar Correction

Perfect for:

- Fixing spelling and grammar mistakes
- Correcting punctuation errors
- Improving sentence structure
- Maintaining original tone and meaning

### AI Content Humanization

Ideal for:

- Making AI-generated content sound more natural
- Adding conversational elements
- Improving readability and flow
- Creating more engaging text

## API Configuration

The application uses Google's Gemini API. The API key is configured in `app.py`. For production use, consider using environment variables for security.

## System Prompts

The application uses carefully crafted system prompts that:

- Avoid markdown formatting (no asterisks or special characters)
- Focus on specific tasks (grammar vs. humanization)
- Maintain original meaning and context
- Provide clean, formatted output

## File Structure

```
Gramzo/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
└── .github/
    └── copilot-instructions.md
```

## Development

To run in development mode:

```bash
python app.py
```

The application will start in debug mode on `http://localhost:5000`.

## Contributing

Feel free to contribute by:

- Improving the UI/UX
- Adding new features
- Optimizing the AI prompts
- Enhancing error handling

## License

This project is open source and available under the MIT License.
