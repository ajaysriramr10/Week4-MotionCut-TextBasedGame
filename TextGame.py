import time

def display_intro():
    print("Welcome to the Challenging Text Adventure Game!")
    print("You find yourself in a dark and treacherous forest. Your survival depends on your choices.")
    print("Make the wrong decisions, and you may never escape this forest. Good luck!\n")

def make_choice(options):
    while True:
        choice = input("Choose an option ({0}): ".format('/'.join(options))).strip().lower()
        if choice in options:
            return choice
        else:
            print("Invalid input. Please choose a valid option.")

def forest_path():
    print("You start walking through the forest...")
    time.sleep(2)
    
    paths = {
        'a': "You take the left path and find a river.",
        'b': "You take the right path and come across a cave.",
        'c': "You venture deeper into the forest and find a mysterious house."
    }
    
    choice = make_choice(paths.keys())
    
    print(paths[choice])
    
    if choice == 'a':
        time.sleep(2)
        print("You can cross the river (A) or follow it downstream (B).")
        choice = make_choice(['a', 'b'])
        
        if choice == 'a':
            print("You try to cross the river but get swept away by the current. Game Over!")
        else:
            print("You follow the river downstream and find a hidden waterfall. You can climb it (A) or go around it (B).")
            choice = make_choice(['a', 'b'])
            if choice == 'a':
                print("You successfully climb the waterfall, but you encounter a dangerous creature on the other side.")
                time.sleep(2)
                print("You have two allies from Clash of Clans, P.E.K.K.A and Wizard, to help you defeat the creature.")
                print("a: Choose P.E.K.K.A to wage war")
                print("b: Choose Wizard to wage war ")
                ally_choice = make_choice(['a', 'b'])
                if ally_choice == 'a':
                    print("You choose P.E.K.K.A, and together you defeat the creature and successfully escape. You win!")
                else:
                    print("You choose Wizard, but the creature proves too powerful, and you are defeated. Game Over.")
            else:
                print("You go around the waterfall and eventually find your way out of the forest. You win!")
    elif choice == 'b':
        time.sleep(2)
        print("You enter the cave and discover a treasure chest guarded by a fierce dragon.")
        time.sleep(2)
        print("You have two options to defeat the dragon:")
        print("a: Use an electro dragon lord of dragons.")
        print("b: Use a little sword.")
        
        dragon_choice = make_choice(['a', 'b'])
        if dragon_choice == 'a':
            print("You summon the electro dragon lord of dragons, which defeats the fierce dragon. You win!")
        else:
            print("You attempt to fight the dragon with the little sword, but it's not enough. The dragon breathes fire on you. Game Over!")
    else:
        time.sleep(2)
        print("You enter the mysterious house. It's dark inside.")
        time.sleep(2)
        print("Do you explore the house (A) or leave immediately (B)?")
        choices = {
            'a': "Explore the house.",
            'b': "Leave immediately."
        }
        choice = make_choice(choices)
        
        if choice == 'a':
            print("You explore the house and discover two different paths:")
            time.sleep(2)
            print("a: Get invisible power and defeat the witch inside the house (Win)")
            print("b: Enter the giant island and get lost (Game Over)")
            
            house_choice = make_choice(['a', 'b'])
            
            if house_choice == 'a':
                print("You find a hidden source of invisible power in the house, use it to defeat the witch, and successfully escape. You win!")
            else:
                print("You enter the giant island and get lost in its vastness. Game Over!")

        else:
            print("You leave the house and eventually find your way out of the forest. You win!")

def main():
    display_intro()
    forest_path()

if __name__ == "__main__":
    main()
