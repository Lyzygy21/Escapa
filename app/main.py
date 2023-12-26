import random
import re

from chat_logic.nlp_processing import tokenize
from chat_logic.conversation import ConversationContext
from chat_logic.intent_recognition.classifier import classify_intent
from chat_logic.get_chat_response import get_chat_response

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
    # Directly use the centralized chat logic
    return get_chat_response(user_input)


if __name__ == "__main__":
    print("The question is the shape of your key, will you escape?")
    print("-----------------Welcome to Escapa---------------------")
    chat()
