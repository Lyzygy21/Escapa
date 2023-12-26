# classifier.py
import re

def classify_intent(user_input):
    """
    Classify the user input into an intent based on patterns/keywords.
    """

    # Patterns for greetings and farewells
    greeting_patterns = r'\b(hello+|hi+|hey+|greetings|what\'s up+)\b'
    farewell_patterns = r'\b(bye+|goodbye+|see you+|farewell|later+)\b'

    user_input_lower = user_input.lower()

    # Check for greeting patterns
    if re.search(greeting_patterns, user_input_lower):
        return "greeting"
    # Check for farewell patterns
    elif re.search(farewell_patterns, user_input_lower):
        return "farewell"
    
    # Add more patterns here

    return "unknown"  # Default if no intent is recognized