import random


def main():
    print("You only have 5 guesses")
    print("-----------------------")
    guess_pokemon = get_pokemon()
    clues = ask_clue(guess_pokemon)
    print(clues)
    print("-----------------------")
    user_guess = guess(guess_pokemon)
    print(user_guess)
    
    
def get_pokemon():
    pokemon = []
    with open("pokemon.txt") as file:
        for line in file:
            pokemon.append(line.rstrip().capitalize())
    
    guess_pokemon = random.choice(pokemon)
    return guess_pokemon
        
        
def ask_clue(guess_pokemon):
    while True:
        clue = input("Do you want clue? [y/n] ").lower()
        if clue == "y":
            return f'''Clues:
{len(guess_pokemon)} letters
First letter is "{guess_pokemon[0]}"
Last letter is "{guess_pokemon[-1].upper()}"'''
        elif clue == "n":
            return "Okay, goodluck!"
        else:
            print("Y for yes and N for no")
            continue

def guess(guess_pokemon):
    guess_count = 0
    while guess_count != 5:
        guess = input("Guess: ").capitalize()
        if guess != guess_pokemon:
            print("Wrong! Try again")
            guess_count += 1
            pass
        else:
            return "Correct!"
        
        if guess_count == 3:
            print("-----------------------")
            clue2 = input("Do you want clue again? [y/n]").lower()
            if clue2 == "y":
                print(f'The second letter was "{guess_pokemon[1].upper()}"')
            print("-----------------------")

    return f"It's {guess_pokemon}!"
            
    
if __name__ == "__main__":
    main()
