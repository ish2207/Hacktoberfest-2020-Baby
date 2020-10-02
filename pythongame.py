import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro(item, option):
    print_pause("You have just arrived at your ground outside your house!\n")
    print_pause("You are at some distance from the door.\n")
    print_pause("There are people around gazing your house and warning you that there is a " + option + " somewhere in the house.\n")
    print_pause("In your left there is a dark cave.\n")
    print_pause("In your hand you hold a light weighted glass rod.\n")

def dark_cave(item, option):
    if "shield" in item:
        print_pause("\nYou enter into the cave.")
        print_pause("\nYou look all around the cave. It's just an empty dark cave!")
        print_pause("\nYou walk back to your house.\n")
    else:
        print_pause("\nYou enter into the cave.")
        print_pause("\nIt is a very small dark cave.")
        print_pause("\nyour eye catches a shining metal behind a rock.")
        print_pause("\nYou have the powerful shield of Captain America!")
        print_pause("\nyYou throw your glass rod and hold that shield.")
        print_pause("\nYou walk back towards your ground.\n")
        item.append("shield")
    ground(item,option)
def house(item, option):
    print_pause("\nYou approach the door of the house.")
    print_pause("\nYou are about to knock when the door "
                "opens and out steps a " + option + ".")
    print_pause("\nEep! This is the " + option + "'s house!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "shield" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "with only a light weighted glass rod.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "shield" in item:
                print_pause("\nAs the " + option + " moves to attack, "
                            "you unsheath your new shield.")
                print_pause("\nThe Shield of Captain America shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("\nBut the " + option + "takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("\nYou have entered in your new safe house now!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your light weighted glass rod is of no match for the "
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been followed up.\n")
            ground(item, option)
            break
def ground(item,option):
    print_pause("\nEnter 1 to knock at the door.")
    print_pause("\nEnter 2 to run into the cave.")
    print_pause("\nWhat would you do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house(item,option)
            break
        elif choice1 == "2":
            dark_cave(item, option)

def play_again():
    again = input("Would you like to play again? (yes/no)").lower()
    if again == "yes":
        print_pause("\n\n\nExcellent! Let's rock again ...\n\n\n")
        play_game()
    elif again == "no":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["thief", "pirate", "murderer", "troll",
                            "kidnapper"])
    intro(item, option)
    ground(item, option)


play_game()
