import random

ascii_cards = {
    2:  "┌─────┐\n│2    │\n│     │\n│  ♠  │\n│     │\n│    2│\n└─────┘",
    3:  "┌─────┐\n│3    │\n│     │\n│  ♣  │\n│     │\n│    3│\n└─────┘",
    4:  "┌─────┐\n│4    │\n│     │\n│  ♣  │\n│     │\n│    4│\n└─────┘",
    5:  "┌─────┐\n│5    │\n│     │\n│  ♣  │\n│     │\n│    5│\n└─────┘",
    6:  "┌─────┐\n│6    │\n│     │\n│  ♣  │\n│     │\n│    6│\n└─────┘",
    7:  "┌─────┐\n│7    │\n│     │\n│  ♣  │\n│     │\n│    7│\n└─────┘",
    8:  "┌─────┐\n│8    │\n│     │\n│  ♣  │\n│     │\n│    8│\n└─────┘",
    9:  "┌─────┐\n│9    │\n│     │\n│  ♣  │\n│     │\n│    9│\n└─────┘",
    10: "┌─────┐\n│10   │\n│     │\n│  ♦  │\n│     │\n│   10│\n└─────┘",
    10: "┌─────┐\n│J   │\n│     │\n│  ♦  │\n│     │\n│   J│\n└─────┘",
    10: "┌─────┐\n│Q   │\n│     │\n│  ♦  │\n│     │\n│   Q│\n└─────┘",
    10: "┌─────┐\n│K   │\n│     │\n│  ♦  │\n│     │\n│   K│\n└─────┘",
    11: "┌─────┐\n│A    │\n│     │\n│  ♥  │\n│     │\n│    A│\n└─────┘",
    1:  "┌─────┐\n│A    │\n│     │\n│  ♣  │\n│     │\n│    A│\n└─────┘",
}

user_cards = []
comp_cards = []

def deal_card():
    """returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    while score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

Game_on = True
while Game_on:
    for cards in user_cards:
         print(ascii_cards[cards])
    print(f"your score: {calculate_score(user_cards)}")
    print(f"Dealer's card: \n{ascii_cards[comp_cards[0]]}")
    user_input = input("type 'y' to get another card or 'n' to pass.")
    if user_input == 'y':
        user_cards.append(deal_card())
        if calculate_score(user_cards) > 21:
            for cards in user_cards:
                print(ascii_cards[cards])
            print("You went over. You lose.")
            exit()
    else: 
        Game_on = False

while calculate_score(comp_cards) < 17:
             comp_cards.append(deal_card())

user_score = calculate_score(user_cards)
comp_score = calculate_score(comp_cards)
print(f"Here are the dealer's cards:")
for cards in comp_cards:
     print(ascii_cards[cards])
             
if comp_score > 21:
     print("You win. The dealer went over.")
elif user_score > 21:
     print("You went over. You loose.")
elif user_score > comp_score:
     print("you win!!")
elif user_score < comp_score:
     print(f"Dealer's score is: {comp_score}")
     print("Dealer wins")
else:
     print("It's a draw")
    
