from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 7, 8, 9, 10, 10, 10, 10]
ace = [11]
game = True
n = 1

def for_result():
    return f"Your final hand: {user_cards}, final score: {user_score}\nComputer's final hand: {computer_cards}, final score: {computer_score}"

def first_result():
    return f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_first_card}"

def deal():
    return random.sample(cards, 2)

def score_user():
    return user_cards[0] + user_cards[1]
def score_computer():
    return computer_cards[0] + computer_cards[1]

def blackjack():
    if (computer_cards == [11, 10] or computer_cards == [10,11]) and (user_cards == [11, 10] or user_cards == [10, 11]):
        print(for_result())
        print("You lose")
        return True
        
    if user_cards == [11, 10] or user_cards == [10, 11]:
        print(for_result())
        print("You win!")
        return True
        
    if computer_cards == [11, 10] or computer_cards == [10, 11]:
        print(for_result())
        print("You lose")
        return True  
    
def check():
    if user_score > 21:
        print(for_result())
        print("You lose") 
        return True 

def zaebalo():
    if user_score > computer_score:
        print(for_result())
        print("You win!")
        return True
                        
    if user_score < computer_score:
        print(for_result())
        print("You lose!")
        return True
                        
    if user_score == computer_score:
        print(for_result())
        print("It is Draw!!")
        return True

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y': 
    clear()
    print(logo)

    user_cards = deal()
    computer_cards = deal()

    user_score = score_user()
    computer_score = score_computer()

    computer_first_card = computer_cards[0]

    print(first_result()) 

if blackjack() == True:
    game = False

while game:
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        n += 1
        user_cards += random.sample(cards, 1)
        user_score += user_cards[n]
        if user_score > 21:
            if user_cards[n] == 11:
                user_cards[n]= 1
                user_score = sum(user_cards)
        print(first_result()) 
        if check() == True:
            game = False 
    else:
        if computer_score < 17:
            computer_cards += random.sample(cards, 1)
            computer_score += computer_cards[2]
            if computer_score > 21:
                print(for_result())
                print("You win!")
                game = False
            else:
                if zaebalo() == True:
                    game = False
        else:
            if zaebalo() == True:
                game = False



    
