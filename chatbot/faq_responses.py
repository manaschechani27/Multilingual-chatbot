import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Define some basic FAQ responses
FAQ_RESPONSES = {
    "hello": "Hi there! How can I assist you today?",
    "bye": "Goodbye! Have a great day!",
    "help": "I can assist with basic queries and reminders.",
    "thanks": "You're welcome!"
}

def generate_response(message):
    # Process the message with spaCy
    doc = nlp(message.lower())
    
    # Look for keywords in the message and return a response
    for token in doc:
        if token.lemma_ in FAQ_RESPONSES:
            return FAQ_RESPONSES[token.lemma_]
    
    # Default response if no keywords are found
    return "Sorry, I didn't understand that. Can you please rephrase?"
