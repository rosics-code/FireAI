from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your OpenAI or API key setup
API_KEY = "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"  # Replace with your actual API key
API_URL = "https://fireai-jpne.onrender.com/api/chat"  # Replace with your actual API URL

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Call your AI API or model here (this example is using a generic API)
    headers = {'Authorization': f'Bearer {API_KEY}'}
    payload = {
        "messages": [{"role": "user", "content": user_message}]
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            ai_reply = response.json().get("reply")
            return jsonify({"reply": ai_reply})
        else:
            return jsonify({"error": "Failed to get AI response"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
