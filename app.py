from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI  # Use OpenRouter API

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (important for frontend-backend communication)

# Set up OpenRouter API
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",  # OpenRouter API URL
    api_key='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'  # Replace with your OpenRouter API key
)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json  # Get the incoming JSON data from the request
    user_message = data.get("message")  # Extract the user message from the JSON payload

    if not user_message:
        return jsonify({"error": "Message is required"}), 400  # Return an error if no message is provided

    try:
        # Call OpenRouter API with the user message
        response = client.chat.completions.create(
            model="sao10k/l3.3-euryale-70b",  # Example model, replace with your model
            messages=[{"role": "user", "content": user_message}]
        )

        # Print the response to the console for debugging
        print(response)

        # Return the AI's reply to the user
        return jsonify({"reply": response['choices'][0]['message']['content']})

    except Exception as e:
        # If an error occurs, print the error and return a generic error message
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong with the AI response."}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
