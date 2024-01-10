import re


def simple_chatbot(user_input):
    # Define rules and responses
    rules = {
         r'(hi|hello|hey|Ram Ram)( there)?': 'Hello There I am Chatbot Created by Shubham,How May I Help You?',
        r'how are you|kaisa Hai': 'I am a chatbot, but thanks for asking!,Mai Accha hu',
        r'your name|Tumhara Naam': 'Mai Shubham Ne Banaya Hua Chatbot Hu',
        r'Connect Me To yash|talk to yash|call yash':'Wo Abhi Bahar Hai!I will Inform Him To Call You',
        r'(ok|Thank you)': 'No Worries!Koi Aur Madad',
        r'(No|no thanks)': 'Ok,Have Nice Day Ahead',
        r'(bye|goodbye|Chal Bye)': 'Goodbye! Have a great day!',
             }#we can add number of rules for our chatbot

    # Check user input against rules
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # If no match found, provide a default response
    return "I am prototype,Mujhe Iska Answer Nahi Pata"


# Main loop for interacting with the chatbot
def main():
    print("Shubham Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Shubham Chatbot: Goodbye!")
            break

        response = simple_chatbot(user_input)
        print("Shubham Chatbot:", response)


