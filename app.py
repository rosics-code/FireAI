from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize the OpenRouter client with your API key
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",  # OpenRouter API URL
    api_key='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'  # Your OpenRouter API Key
)

@app.route('/api/chat', methods=['POST'])  # This is the POST route your frontend will call
def chat():
    data = request.json  # Get the incoming JSON data
    user_message = data.get("message")  # Extract the message sent by the user

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        # Send request to OpenRouter's API for completion
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",  # Replace with your model
            messages=[{"role": "user", "content": user_message}]
        )

        return jsonify({"reply": response['choices'][0]['message']['content']})  # Return AI response

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Error handling if something goes wrong

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)  # Running on all network interfaces for external access
