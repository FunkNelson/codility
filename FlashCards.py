import random

cardStack = {
    'Golden Signals': 'Latency, Traffic, Error Rates, Saturation',
    'Latency': 'Time it takes for a request to travel from the client to the server and back',
    'Traffic': 'Number of requests a system receives over a specific period',
    'Errors (Monitoring)': 'Percentage of requests resulting in errors, such as 404 Page Not Found or 500 Internal Server errors',
    'Saturation': 'Measures resource utilization, including CPU, memory and disk space',
    'Subnet': 'CIDR block portion of a VPC\nLives in Availability Zones\nPublic: Has route to Internet Gateway\nPrivate: Does not have route to Internet Gateway'
}


keys_list = list(cardStack.keys())
width = 50
session_active = True


def displayCard(card):
    print('\n')
    print(f" ------------------------------------------------ ")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(card.center(width))
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f" ------------------------------------------------ ")
    input('Press Enter to flip the card')


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
