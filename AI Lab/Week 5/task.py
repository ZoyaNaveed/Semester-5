# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:11:34 2023

@author: LENOVO
"""

import random

# Define a dictionary of predefined responses
responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm just a chatbot, but I'm here to assist you.",
    "bye": "Goodbye! Have a great day!",
}

# Function to get a response from the chatbot
def get_response(user_input):
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that. Please ask me something else.")

# Main chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
