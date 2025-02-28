from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

# Initialize Flask app
app = Flask(__name__)

CORS(app)

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",  # OpenRouter API base URL
  api_key="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",  # Replace with your actual OpenRouter API key
)

# Route for handling chat messages
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json  # Get the incoming JSON data from the request
    user_message = data.get("message")  # Extract the user message from the JSON payload

    if not user_message:
        return jsonify({"error": "Message is required"}), 400  # Return an error if no message is provided

    try:
        # Call DeepSeek R1 Free model via OpenRouter API
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",  # Using DeepSeek R1 Free model
            messages=[{"role": "user", "content": user_message}]
        )

        # Return the AI's reply to the user
        return jsonify({"reply": completion.choices[0].message.content})

    except Exception as e:
        # If an error occurs during the API call, return the error message
        return jsonify({"error": str(e)}), 500

# Start the Flask app on the correct port (Render will use an environment variable for the port)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
