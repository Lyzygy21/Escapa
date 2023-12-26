class ConversationContext:
    def __init__(self):
        self.last_topic = None
        self.greeting_count = 0

    def update_topic(self, topic):
        if topic == "greeting":
            if self.last_topic == "greeting":
                self.greeting_count += 1
            else:
                self.greeting_count = 1
        else:
            self.greeting_count = 0
        self.last_topic = topic

    def get_response(self, user_input):
        if self.last_topic == "greeting" and self.greeting_count > 1:
            return "We already said hello, let's chat about something else!"
        return None