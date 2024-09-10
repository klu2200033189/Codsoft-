def chatbot():
    print("Chatbot: Hello! I'm a simple rule-based chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase to handle case-insensitive matching

        # Predefined responses based on user input
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but thanks for asking! How can I help you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that. Could you please ask something else?")


# Run the chatbot
chatbot()
