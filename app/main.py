
def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = process_input(user_input)
        print(f"Escapa: {response}")

def process_input(user_input):
    # Simple response logic, can be expanded later
    if "hello" in user_input.lower():
        return "Hello there!"
    else:
        return "working on expanding capabilities"

if __name__ == "__main__":
    print("The question is the shape of your key, will you escape?")
    print("-----------------Welcome to Escapa---------------------")
    chat()
