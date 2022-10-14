"""
Chatbot Steps
1. Input/Listen
2. Process/Decide
3. Output/Talkback
"""


def listen():
    return input("Say Something : ")


# Conversation type words
greet_words = ['Hi', 'Hello', 'Yo']
bye_words = ['Bye', 'See you', 'Chat to you soon']


def decide(command):
    words_divider = command.split(" ")
    print(words_divider)


def talkback():
    pass


# Listening command
command = listen()

# Deciding
decide(command)
