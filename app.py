# app.py
import os
from flask import Flask, request, jsonify # type: ignore
from dotenv import load_dotenv  # type: ignore

# --- LLM API Client Setup ---
# Google Gemini (requires google-generativeai library)
import google.generativeai as genai # type: ignore

# Load environment variables (for local testing, .env file)
load_dotenv()

# --- Initialize LLM Client ---
# Google Gemini
gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key:
    try:
        genai.configure(api_key=gemini_api_key)
        llm_client = genai.GenerativeModel('gemini-2.0-flash')
        print("Gemini client initialized.")
    except Exception as e:
        llm_client = None
        print(f"Errror initializing Gemini client: {e}")
else:
    llm_client = None
    print("Warning: GEMINI_API_KEY not found. LLM client not initialized.")


app = Flask(__name__)

@app.route('/')
def home():
    return "LLM API is running! Use /generate to get a response."

@app.route('/generate', methods=['POST'])
def generate_text():
    if llm_client is None:
        return jsonify({"error": "LLM API key not configured."}), 500

    try:
        data = request.get_json(force=True)
        prompt = data.get('prompt')

        if not prompt:
            return jsonify({"error": "Prompt is required."}), 400

        print(f"Received prompt: {prompt}")

        # --- Call LLM API ---
        # Google Gemini
        response = llm_client.generate_content(prompt, generation_config={"max_output_tokens": 100})
        generated_text = response.text

        return jsonify({"generated_text": generated_text})

    except Exception as e:
        print(f"Error during generation: {e}")
        return jsonify({"error": str(e), "message": "Failed to generate text."}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
