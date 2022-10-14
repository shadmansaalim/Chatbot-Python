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
bad_words = ['kill', 'bitch', 'fuck']


def decide(command):
    # Converting everyting to lower case for simplicity and match
    command = command.lower()
    words_divider = command.split(" ")
    for word in words_divider:
        if word in greet_words:
            talkback("Hi mate, how's it going.")
            break
        elif word in bye_words:
            talkback("It was nice talking to you. Bye take care.")
            break
        elif word in bad_words:
            talkback("Please talk in a good way mate, you are using bad words.")
            break


def talkback(response):
    print(response)


# Chatbot
while True:
    # Listening command
    command = listen()
    # Deciding
    decide(command)
