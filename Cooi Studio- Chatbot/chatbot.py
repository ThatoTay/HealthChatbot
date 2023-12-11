import nltk
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import json
import random
from nltk import word_tokenize, pos_tag

# Load intents from the JSON file
with open('intents.json') as file:
    intents = json.load(file)

def process_input(user_input):
    tokens = word_tokenize(user_input)
    tagged_tokens = pos_tag(tokens)
    return tagged_tokens

def recognize_intent(tagged_tokens):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if all(word.lower() in user_input.lower() for word in pattern.split()):
                return intent
    return None

def generate_response(intent_tag):
    for intent in intents['intents']:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])
    return "I'm sorry, I couldn't understand that. If you have health concerns, please provide more information."

print("|============= Welcome to Healthcare Chatbot System! =================|")
print("|============================== Feel Free ============================|")
print("|================================== To ===============================|")
print("|================ Ask any query about your Health ====================|")
print("|==================== WE WILL TRY TO ASSIST YOU ======================|")

# Main loop
while True:
    user_input = input("User: ")

    # Process user input and recognize intent
    processed_input = process_input(user_input)
    matched_intent = recognize_intent(processed_input)

    # Check if user wants to exit
    if matched_intent and matched_intent['tag'] in ['goodbye', 'bye', 'see ya']:
        print("Bot: Take care of your health. Goodbye!")
        print("Your Health, Our Priority: Chatbot Care, Always there!")
        break

    # Generate response based on the recognized intent
    if matched_intent:
        response = generate_response(matched_intent['tag'])
    else:
        response = "I'm sorry, I couldn't understand that. If you have health concerns, please provide more information."

    # Display the bot's response
    print("Bot:", response)
