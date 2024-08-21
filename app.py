from flask import Flask, request, jsonify
from chatbot.faq_responses import generate_response
from chatbot.language_support import translate_message

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Multilingual Chatbot!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    lang = request.json.get('lang', 'en')  # Default to English if no language is specified
    
    # Translate message to English if it's in Japanese
    if lang == 'ja':
        user_message = translate_message(user_message, 'ja', 'en')
    
    # Generate chatbot response
    bot_reply = generate_response(user_message)
    
    # Translate response back to Japanese if needed
    if lang == 'ja':
        bot_reply = translate_message(bot_reply, 'en', 'ja')
    
    response = {"reply": bot_reply}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
