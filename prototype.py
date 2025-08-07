import json as js
import random

def choice(doing, sets): # Puts the corresponding values according to the choice
    match doing:
        case 'A': # Makes a new set
            name = input("What is the name of the new set? ")
            while name not in sets:
                print("Set already exists")
                name = input("What is the name of the new set? ")            
            cards = {}
            count = 1
        case 'B': # Gets cards == set name
            print("Available sets:")
            first = True
            for x in sets.keys(): # Prints out all the default values excluding the first one
                if not first:
                    print(x)
                else:
                    first = False
            name = input("What set would you like to Modify? ")
            while name not in sets:
                print("Set not available")
                name = input("What set would you like to Modify? ")
            cards = sets[name]
            count = cards["count"]            
        case 'C':
            print("Available sets:")
            first = True
            for x in sets.keys(): # Prints out all the default values excluding the first one
                if not first:
                    print(x)
                else:
                    first = False
            name = input("What set would you like to study? ")
            while name not in sets:
                print("Set not available")
                name = input("What set would you like to study? ")
            cards = sets[name]
            count = cards["count"]
    return cards, name, count

def modify(file, cards, name, count, sets): # deletes set/card or adds card
    choice = input("How would you like to modify the set?\nA: Add card\nB: Delete card\nC: Delete set\n")
    match choice:
        case 'A':
            add_card(file, cards, name, count, sets)
        case 'B':
            del_card(file, cards, sets, name)
        case 'C':
            del sets[name]
            print("Deleted set")
            file.truncate(0)
            js.dump(sets, file, indent= 4) # writes it to the file
            file.seek(0)
    return

def add_card(file, cards, name, count, sets): # adds a card to the set
    ques = input("You can now add a question (Q to quit): ") # Gets the question
    while ques != 'Q': # adds the question and answer as a tuple into the cards dict
        ans = input("You can now add an answer: ")
        cards["Question " + str(count)] = (ques, ans)
        count += 1
        ques = input("You can now add a question (Q to quit): ")
    cards["count"] = count
    sets[name] = cards # gets the set name == to the cards dict
    js.dump(sets, file, indent= 4) # writes it to the file
    file.seek(0)
    return

def study(cards, count): # Goes through all the cards
    numbers = [x for x in range(1,count)] # Puts all the numbers into a list
    for x in range(count - 1): # Goes through all the numbers
        num = random.choice(numbers) # Gets a random number
        numbers.remove(num) # Removes that number so it doesn't pop up again
        flash_card = cards["Question " + str(num)] # Gets the actual card
        print("The Question is: " + flash_card[0]) # Prints out the question and answer
        input("Enter to flip")
        print("The Answer is: " + flash_card[1])
        print()

def del_card(file, cards, sets, name): # Deletes the card from the set
    print("Cards in set: ") # Prints out all the cards
    for x in cards.keys():
        if(x != "count"):
            print(f"{x}\n    Q: {cards[x][0]}\n    A: {cards[x][1]}")
        
    num = input("Which card would you like to delete (Q to quit)? (number): ") # Gets card number
    while num != 'Q' and len(cards) > 1: # if they didn't quit or if the set isn't empty
        while "Question " + num not in cards: # Checks if num is a valid number
            print("Card not available")
            num = input("Which card would you like to delete? (number): ")
        del cards["Question " + num] # Deletes the card
        for x in range(int(num), len(cards)): # Fixes all the card numbers
            cards["Question " + str(x)] = cards["Question " + str(x + 1)]
            del cards["Question " + str(x + 1)]
        for x in cards.keys(): # Prints out all the cards
            if(x != "count"):
                print(f"{x}\n    Q: {cards[x][0]}\n    A: {cards[x][1]}")
        num = input("Which card would you like to delete (Q to quit)? (number): ")
    cards["count"] = len(cards) # changes count to proper length of set
    sets[name] = cards # updates sets
    file.truncate(0)
    js.dump(sets, file, indent= 4) # writes it to the file
    file.seek(0)
    return


file_name = "test.json"
file = open("test.json", 'r+')
sets = js.load(file)  # Put the entire text file into a dict (maybe too much memory?)
file.seek(0) # Goes back to the beginning
doing = input("What would you like to do:\nA: Make a new set\nB: Modify Set\nC: Study cards\nQ: Quit\n")
while doing != "Q":
    cards, name, count = choice(doing, sets)
    if doing == 'A':
        add_card(file, cards, name, count, sets)
    elif doing == 'B':
        modify(file, cards, name, count, sets)
    elif doing == 'C': # Prints out all the cards in a random order
        study(cards, count)
    doing = input("What would you like to do:\nA: Make a new set\nB: Modify Set\nC: Study cards\nQ: Quit\n")

file.close()