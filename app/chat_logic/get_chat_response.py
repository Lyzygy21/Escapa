from .conversation import ConversationContext
from .intent_recognition.classifier import classify_intent
# Add other necessary imports based on your chatbot's logic
import random
# Assuming you have a global conversation context
conversation_context = ConversationContext()

def get_chat_response(user_input):
    """
    Process the user input and return the chatbot's response.
    """
    # Classify the intent of the user input
    intent = classify_intent(user_input)

    # Update the conversation topic and check for context-specific responses
    conversation_context.update_topic(intent)
    context_response = conversation_context.get_response(user_input)
    if context_response:
        return context_response

    # Respond based on the identified intent
    if intent == "greeting":
        # Use a varied response for greetings
        return random.choice(["Hello! How can I help you?", "Hi there! What can I do for you?", "Greetings!"])
    elif intent == "farewell":
        return "Goodbye! Have a great day!"
    else:
        return "I'm still learning, but I'm getting better every day!"