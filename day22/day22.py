from sys import path
import re

with open(path[0] + '/input.txt') as f:
    deck1, deck2 = [[int(y) for y in x.split()] for x in re.findall(r'Player \d:\n((?:\d\n?)+)', f.read())]

def combat(deck1, deck2):
    while deck1 and deck2:
        card1, deck1 = deck1[0], deck1[1:]
        card2, deck2 = deck2[0], deck2[1:]
        if card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]
    if deck1:
        return 1, deck1
    elif deck2:
        return 2, deck2

def recursive_combat(deck1, deck2):
    history = []
    while deck1 and deck2:
        if (deck1, deck2) in history:
            return 1, deck1
        history.append((deck1, deck2))
        card1, deck1 = deck1[0], deck1[1:]
        card2, deck2 = deck2[0], deck2[1:]
        winner = 0
        if card1 <= len(deck1) and card2 <= len(deck2):
            winner, _ = recursive_combat(deck1[:card1], deck2[:card2])
        if winner == 1 or (winner == 0 and card1 > card2):
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]
    if deck1:
        return 1, deck1
    elif deck2:
        return 2, deck2

def winning_score(deck):
    return sum(i * deck[-i] for i in range(1, len(deck) + 1))

winner, deck = combat(deck1, deck2)
print(winner, winning_score(deck))
winner, deck = recursive_combat(deck1, deck2)
print(winner, winning_score(deck))