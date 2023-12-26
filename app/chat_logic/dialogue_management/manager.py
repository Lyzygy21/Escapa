# manager.py
import random
from app.main import greeting_responses

def get_response(intent, user_input, conversation_context):
    """
    Generate a response based on the identified intent and conversation context.
    """

    if intent == "greeting":
        return handle_greeting(conversation_context)
    elif intent == "farewell":
        return handle_farewell(conversation_context)
    # Add more intents here
    else:
        return handle_unknown()

def handle_greeting(conversation_context):
    return random.choice(greeting_responses)

def handle_farewell(conversation_context):
    # Example response logic for farewell
    return "Goodbye! Have a great day!"

def handle_unknown():
    # Default response for unrecognized intents
    return "I'm not sure I understand, but I'm learning more every day!"