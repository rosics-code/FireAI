from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<OPENROUTER_API_KEY>",
)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://fireai-sepia.vercel.app/",
                "X-Title": "AI Chatbot",
            },
            model="sao10k/l3.3-euryale-70b",
            messages=[{"role": "user", "content": user_message}]
        )
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
