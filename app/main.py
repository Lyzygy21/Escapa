import random
import re

from chat_logic.nlp_processing import tokenize
from chat_logic.conversation import ConversationContext

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
   # Check for context-based responses first
    context_response = conversation_context.get_response(user_input)
    if context_response:
        # If context-aware response is given, reset the topic
        conversation_context.update_topic(None)
        return context_response

    # Regular input processing
    tokens = tokenize(user_input.lower())
    if any(word in tokens for word in ["hello", "hi", "greetings"]):
        # Update topic only if a new greeting is detected
        if conversation_context.last_topic != "greetings":
            conversation_context.update_topic("greetings")
        return random.choice(greeting_responses)
    else:
        return "I'm still learning, but I'm getting better every day!"

if __name__ == "__main__":
    print("The question is the shape of your key, will you escape?")
    print("-----------------Welcome to Escapa---------------------")
    chat()
