import re
import json
import random


def bot_response():
        print("\nBot: Hello there!👋  \nPlease Enter your name .. 😍")
bot_response()

def input_name():
        
        user_name = input("You: ")
        print("Nice to meet you",user_name,"..!!")
        print("Please provide your number")
        user_no = input("You: ")
        print("Also provide your email so we can send you the best offers..")
       
input_name()


def input_email():
        user_mail = input("You: ")
        print("Superb..So would you like to travel International Gateways ? \n Please type y/n..")
input_email()

def random_response():
    random_list = [
        "Please try writing something that i understand.",
        "Oh! It appears you wrote something I don't understand yet",
        "I'm sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]

    list_count = len(random_list) # it will give 4 as the length beacuse 0-4 is the sentence range
    random_item = random.randrange(list_count) # it will randomly choose any number from the range of 4
    # print(random_item)
    return random_list[random_item] #randomly bot will reply to the not specified ques from one of those sentences


def json_file(file):
    with open(file) as bot_responses:
        # print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


#storing data in a variable
response_data = json_file(r"bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

   
    for response in response_data:
        response_score = 0

        required_score = 0
        required_words = response["required_words"]

        # if required words exists
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1
       
        # in this condition if the count of required words from user input is same as the count of required word in json file
        if required_score == len(required_words):
            # print(len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response then add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to the list counting the total of words matched in user input
        score_list.append(response_score)
        # print(response_score, response["user_input"])
        # print(score_list)
    # it will get the response in which max of the user responded words are matched
    best_response = max(score_list)
    # print(best_response)
    #it will return the index number of the list in which the max responded words are matched
    response_index = score_list.index(best_response)
    # print(response_index)
   
    # if user enters no input
    if input_string == "":
        return "Please type something!!"

    # if the user matches input found in json file then it returns the respective index bot response
    if best_response != 0:
        return response_data[response_index]["bot_response"]
    #if nothing matched then it will return the random responses
    return random_response()


while True:
    user_input = input("You: ")
    print("\n")
    print("Bot:", get_response(user_input))
    if user_input == 'exit':
        break
    if user_input == 't1':
        break
    elif user_input == 't2':
        break
    elif user_input == 't3':
        break
