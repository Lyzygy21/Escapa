class ConversationContext:
    def __init__(self):
        self.last_topic = None

    def update_topic(self, topic):
        self.last_topic = topic

    def get_response(self, user_input):
        # Check for repeated greetings
        if "hello" in user_input.lower() and self.last_topic == "greetings":
            return "We already said hello, let's chat about something else!"
        return None