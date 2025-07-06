# Simple Rule-Based Chatbot using if-elif-else
# Task 8: Build a Chatbot (ElevateLabTask - 8)

def chatbot():
    print("Hi! I'm ChatBuddy 🤖. Type 'exit' to end the chat.")

    while True:
        # Get user input and convert to lowercase for case-insensitive matching
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "exit":
            print("ChatBuddy: Goodbye! Have a nice day 😊")
            break

        # Greeting
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBuddy: Hello there! How can I assist you today?")

        # Ask about bot's condition
        elif "how are you" in user_input:
            print("ChatBuddy: I'm just a bunch of Python code, but I'm doing great!")

        # Ask for bot's name
        elif "your name" in user_input:
            print("ChatBuddy: I'm ChatBuddy, your friendly chatbot.")

        # Help command
        elif "help" in user_input:
            print("ChatBuddy: You can try asking things like 'what's your name?', 'how are you?', or say 'hello'.")

        # Weather-related message
        elif "weather" in user_input:
            print("ChatBuddy: I can't predict the weather, but it's always sunny in this chat! ☀️")

        # Unknown input
        else:
            print("ChatBuddy: Sorry, I didn't understand that. Can you try something else?")

# Entry point
if __name__ == "__main__":
    chatbot()
