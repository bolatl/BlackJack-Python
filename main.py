from art import  logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True

def get_card():
    return random.choice(cards)

def res(player, comp):
    if sum(player) > 21:
        print("You went over. You lose(")
    elif sum(comp) > 21 or sum(comp) < sum(player):
        print("You won!")
    elif sum(comp) < sum(player):
        print("You lose(")
    else:
        print("It's a draw.")

while play:
    print(logo)
    player = [get_card(), get_card()]
    comp = [get_card()]
    print(f"Your cards: {player}")
    print(f"Dealer's first card {comp}")

    an = input("Type 'y' to get another card, type 'n' to pass: ")
    while an == "y" and len(player) <= 5 and sum(player) < 22:
        player.append(get_card())
        while sum(player) > 21 and 11 in player:
            player[player.index(11)] = 1
        print(f"Your cards: {player}")
        if sum(player) > 21:
            break
        an = input("Type 'y' to get another card, type 'n' to pass: ")

    while sum(comp) < 17:
        comp.append(get_card())
        if sum(comp) > 21 and 11 in comp:
            player[comp.index(11)] = 1

    print(f"Your final cards: {player}")
    print(f"Computer's final cards {comp}")

    res(player, comp)

    ans = input("Do you want to play again? Type 'y', if so: ")
    if ans != 'y':
        play = False
    player.clear()
    comp.clear()