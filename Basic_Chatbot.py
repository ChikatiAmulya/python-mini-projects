def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to end the conversation")

    while True:
        user_message=input("You:").lower()
        if user_message == "hello":
            print("Chatbot: Hi!")
        elif user_message == "how are you?":
            print("Chatbot: I'm doing well,thank you!")
        elif user_message == "what is your name?":
            print("Chatbot: I'm a simple Chatbot created by OpenAI")
        elif user_message == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that")
chatbot()
