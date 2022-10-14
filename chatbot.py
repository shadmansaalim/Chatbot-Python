"""
Chatbot Steps
1. Input/Listen
2. Process/Decide
3. Output/Talkback
"""


def listen():
    return input("Say Something : ")


# Conversation type words
greet_words = ['hi', 'hello', 'yo']
bye_words = ['bye', 'see you', 'chat to you soon']


def decide(command):
    # Converting everyting to lower case for simplicity and match
    command = command.lower()
    words_divider = command.split(" ")
    for word in words_divider:
        if word in greet_words:
            print("Thank you for greeting me")
        elif word in bye_words:
            print("It was nice talking to you. Bye take care.")


def talkback():
    pass


# Listening command
command = listen()

# Deciding
decide(command)
