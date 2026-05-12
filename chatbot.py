import random

# Chatbot Responses
responses = {
    "hi": ["Hello!", "Hi there!", "Welcome!"],
    "hello": ["Hello!", "How can I help you?"],
    "bye": ["Goodbye!", "Take care!"],
    "thanks": ["You're welcome!", "Happy to help!"],
    "ai": ["AI means Artificial Intelligence."],
    "product": ["We provide laptops, mobiles, and accessories."],
    "price": ["Prices depend on the product model."],
    "delivery": ["Delivery takes 3 to 5 days."],
    "support": ["Contact us at support@email.com"],
    "order": ["Your order is currently being processed."],
    "return": ["Products can be returned within 7 days."]
}


# Chatbot Function
def chatbot(user_input):

    user_input = user_input.lower()

    for word in responses:

        if word in user_input:

            return random.choice(responses[word])

    return "Sorry, I don't understand."


# Main Program
print("===== Customer Support Chatbot =====")
print("Type 'bye' to exit")

while True:

    user = input("\nYou: ")

    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    print("Bot:", chatbot(user))