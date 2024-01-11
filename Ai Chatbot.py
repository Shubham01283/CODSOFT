import re


def Shubham_chatbot(user_input):
    # Define rules and responses
    rules = {
        r'(hi|hello|hey|Ram Ram)( there)?': 'Ram Ram! I am Shubham!! How May I Help You?',
        r'how are you|Kaisa Hai': 'Mai Chatbot Hu, but thanks for asking!',
        r'Wassup|Kya Kar Rahe Ho': 'Talking with you',
        r'Call yash|Yash Ko Call Karo': 'Yash Abhi Bahar Hai!! I will Tell Him To Call You,anything else',
        r'your name|Tumhara Naam': 'I am a Shubham Your Personal rule-based chatbot.',
        r'ok|thik hai': 'Anything Else.',
        r'(No thanks|No thank you|bye|goodbye|Chal Bye)': 'Bye Byeji! Have a great day ahead!'
    }

    # Check user input against rules
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # If no match found, provide a default response
    return "I am prototype,Mujhe iska jawab Nhi Pata"


# Main loop for interacting with the chatbot
def main():
    print("Shubham's Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Shubham's Chatbot: Goodbye!")
            break

        response = Shubham_chatbot(user_input)
        print("Shubham's Chatbot:", response)


if __name__ == "__main__":
    main()
