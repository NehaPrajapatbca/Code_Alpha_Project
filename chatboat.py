def chatbot():
    print("ChatBot: Hello! Ask me something. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("ChatBot: Hi there!")
        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks for asking!")
        elif user_input == "bye":
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
