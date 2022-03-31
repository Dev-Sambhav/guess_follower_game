from art import logo,vs
from game_data import data
from random import randint
import os

score = 0
def random_user_data():
    random_number = randint(0,len(data)-1)
    name = data[random_number]['name']
    description = data[random_number]['description']
    country = data[random_number]['country']
    follower = data[random_number]['follower_count']
    return [name,description,country,follower]

def user_A_data(user):
    print(f"Compare A: {user[0]}, a {user[1]}, from {user[2]}")
    return user[3]
def user_B_data(user):
    print(f"Against B: {user[0]}, a {user[1]}, from {user[2]}")
    return user[3]

def check_answer(user_answer,user_A_follower,user_B_follower):
    global score
    if(user_answer == "a"):
        if(user_A_follower>user_B_follower):
            score += 1
            return f"You're right! Current score is: {score}"
        else:
            return f"Sorry, that's wrong. Final score: {score}"
    elif(user_answer == "b"):
        if(user_A_follower<user_B_follower):
            score += 1
            return f"You're right! Current score is: {score}"
        else:
            return f"Sorry, that's wrong. Final score: {score}"
    else:
        return "Please type 'A' or 'B' "

def compare_user():
    user = random_user_data()
    user_A_follower = user_A_data(user)
    print(user_A_follower)
    print(vs)
    user = random_user_data()
    user_B_follower = user_B_data(user)
    print(user_B_follower)
    return user_A_follower,user_B_follower

print(logo)

def game():
    user_A_follower, user_B_follower = compare_user()
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    answer = check_answer(user_answer,user_A_follower,user_B_follower)
    os.system("cls")
    print(logo)
    print(answer)
    return answer

is_end = False
while (not is_end):
    final_answer = game()
    if ("Sorry" in final_answer):
        is_end = True
    else:
        is_end = False



