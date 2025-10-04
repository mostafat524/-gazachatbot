import os
from flask import Flask, render_template, request, jsonify

app = Flask(name)

@app.route('/')
def home():
    return "GAZA 101 Chatbot - Basic version working!"

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "message": "Server is running"})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').lower() if data else ''

        print(f"Received message: {user_message}")

#Simple responses for testing
        if 'water' in user_message:
            return jsonify({'response': '💧 Water crisis information would go here'})
        elif 'food' in user_message:
            return jsonify({'response': '🌾 Food security information would go here'})
        elif 'health' in user_message:
            return jsonify({'response': '🏥 Healthcare information would go here'})
        else:
            return jsonify({'response': 'Hello! I am GAZA 101. Ask me about water, food, or health issues.'})

    except Exception as e:
        print(f"Error in chat: {e}")
        return jsonify({'response': 'Sorry, I encountered an error. Please try again.'})

if name == 'main':
    port = int(os.environ.get("PORT", 7860))
    print(f"🚀 Starting basic GAZA 101 Assistant...")
    app.run(debug=False, host='0.0.0.0', port=port)
