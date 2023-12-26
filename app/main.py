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
    intent = classify_intent(user_input)

    # Update the conversation topic based on the identified intent
    conversation_context.update_topic(intent)

    # Check for context-based responses (handles repeated greetings)
    context_response = conversation_context.get_response(user_input)
    if context_response:
        return context_response

    # Respond based on the identified intent
    if intent == "greeting":
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
