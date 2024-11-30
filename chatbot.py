import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem.",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
def start_chat():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bye! Take care.")
            break
        response = chatbot.respond(user_input)
        if response:
            print("Bot:",response)
        else:
            print("Bot: I didn't understand that.")
        

if __name__ == "__main__":
    start_chat()