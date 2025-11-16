import random
import os

cardStack = {
    'Golden Signals': 'Latency, Traffic, Error Rates, Saturation',
    'Latency': 'Time it takes for a request to travel from the client to the server and back',
    'Traffic': 'Number of requests a system receives over a specific period',
    'Errors (Monitoring)': 'Percentage of requests resulting in errors, such as 404 Page Not Found or 500 Internal Server errors',
    'Saturation': 'Measures resource utilization, including CPU, memory and disk space'
}


keys_list = list(cardStack.keys())


terminal_width = os.get_terminal_size().columns
session_active = True


def displayCard(card):
    print('\n')
    print(f" ------------------------------------------------- ".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(card.center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f" ------------------------------------------------- ".center(terminal_width))
    print('\n')
    input('Press Enter to flip the card'.center(terminal_width))


def printAnswer(card):
    print('\n')
    print(cardStack[card])
    print('\n')


while session_active:
    random_card = random.choice(keys_list)
    displayCard(random_card)
    printAnswer(random_card)
    nextCard = input('Another card? (Y/N)'.center(terminal_width))
    if nextCard.lower() == 'n':
        session_active = False
