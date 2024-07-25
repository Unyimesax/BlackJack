import random



# Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
# game_over = True









# After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.

#Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
# while not game_over:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
cpu_cards = []
ace = 11


#Create a function that uses the List below to *return* a random card.
def deal_card(cards):
    return random.choice(cards)

# Deal both user and computer a starting hand of 2 random card values.
for i in range(2):
    user_cards.append(deal_card(cards))
    cpu_cards.append(deal_card(cards))


#Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
def calculate_score(chosen_card):
    score = 0
    for item in chosen_card:
        score += item
    return score

# Calculate the user's and computer's scores based on their card values.
user_score = calculate_score(user_cards)
cpu_score = calculate_score(user_cards)

# Detect when computer or user has a blackjack. (Ace + 10 value card).
# If computer gets blackjack, then the user loses (even if the user also has a blackjack).
# If the user gets a blackjack, then they win (unless the computer also has a blackjack).
if cpu_score == 21:
    print("Black Jack. Computer Wins.")
    # game_over = True
elif user_score == 21:
    print("Black Jack. You Win.")
    # game_over = True

# If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
if ace in user_cards and user_score > 21 or ace in cpu_cards and cpu_score > 21:
    ace = 1

def another_card():
    return deal_card(cards)

# Reveal User's cards and computer's first card to the user.
print(f"Your cards : {user_cards}. Your score: {user_score}.\n")
print(f"Computer's first card is  {cpu_cards[0]}.\n")

def check_score(user_score, cpu_score):
    if user_score == cpu_score :
        print("It's a draw.")
    elif user_score <= 21 and user_score > cpu_score:
        print("You Win.")
    elif cpu_score <= 21 and cpu_score > user_score:
        print("You lose.")
    elif user_score > 21:
        print("You lose. You went over 21")
    else:
        print("You Win. Computer went over 21.")
        
while user_score < 21:

    # Ask the user if they want to get another card.
    ask_deal = input("Type 'y' to get another card or type 'n' to pass.").lower()

    if ask_deal == 'y':
        user_cards.append(another_card())
        user_score = calculate_score(user_cards)
        
        # Once the user is done and no longer wants to draw any more cards, let the computer play.
        #The computer should keep drawing cards unless their score goes over 16.
    else:
        while cpu_score < 16:
            cpu_cards.append(another_card())
            cpu_score = calculate_score(cpu_cards)

            
# Compare user and computer scores and see if it's a win, loss, or draw.

# Print out the player's and computer's final hand and their scores at the end of the game.
print(f"computer's cards : {cpu_cards}. Computer's score is: {cpu_score}.\n")
print(f"Your cards : {user_cards}. Your score: {user_score}.\n")
check_score(user_score, cpu_score)
    # game_over = True