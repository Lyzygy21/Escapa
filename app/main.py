import random
import re

from chat_logic.nlp_processing import tokenize
from chat_logic.conversation import ConversationContext
from chat_logic.intent_recognition.classifier import classify_intent

conversation_context = ConversationContext()
greeting_responses = ["Hello there!", "Hi, how can I help you?", "Greetings!"]

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = process_input(user_input)
        print(f"Escapa: {response}")

def process_input(user_input):
       # Use the classifier to identify the intent
    intent = classify_intent(user_input)

    # Respond based on the identified intent
    if intent == "greeting":
        # Check if we already responded to a greeting
        if conversation_context.last_topic == "greetings":
            return "We already said hello, let's chat about something else!"
        else:
            conversation_context.update_topic("greetings")
            return random.choice(greeting_responses)
    elif intent == "farewell":
        return "Goodbye! Talk to you later."
    elif intent == "question":
        return "That's an interesting question. Let me think about it."
    else:
        return "I'm still learning, but I'm getting better every day!"

if __name__ == "__main__":
    print("The question is the shape of your key, will you escape?")
    print("-----------------Welcome to Escapa---------------------")
    chat()
