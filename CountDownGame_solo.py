# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 15:32:33 2025

@author: Peter
"""

# simple implementation of the classic Countdown game

# library imports -------------------------------------------------------------
import pickle
import random
import os

from datetime import datetime

from collections import Counter


# function definitions --------------------------------------------------------

def load_anagram_dict(filename: str) -> dict:
    """
    Loads an anagram dictionary from a pickle file.
    
    Parameters:
    - filename: Name of the pickle file to load.
    
    Returns:
    - The loaded anagram dictionary.
    """
    with open(filename, 'rb') as f:
        d = pickle.load(f)
    
    # print(f"Anagram dictionary loaded from '{filename}'.")
    return d

def load_highscores(filename="highscores.pkl") -> list[tuple[str, int]]:
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    else:
        return []

def clear_screen():
    """
    clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def play_round()-> (int,int):
    """
    one round of Countdown
    returns score equal to word length of player, if valid, i.e. if it
    is in the dictionary
    """
    
    valid_letters = False
    
    while not valid_letters:
        letters_drawn = tuple(sorted(random.choices(letter_pool,k=11)))
    
        num_vowels = sum(1 for letter in letters_drawn if letter in vowels)
        
        if num_vowels > 0:
            valid_letters = True
        
    # score for the current round
    score = 0
    
    print("\nHere are the letters to choose from. Good luck!\n")
    print(*letters_drawn)

    guess_player = tuple(sorted(input("\nType your word: ").strip().lower()))
    
        
    # determine winner
    len_guess = len(guess_player)
    
    # validate guesses
    if guess_player not in d or not Counter(guess_player) <= Counter(letters_drawn):
        print("Invalid word!")
        score = 0 # give 0 points if the word is invalid
    else:
        score = len_guess
        
    print("\nYour score for this round:", score,"point(s)\n")
    # Using a random approach to possibly find longer words than the player
    guesses_AI = []
    
    word_length = min(len_guess+1,11)
    
    for j in range(word_length,11):
        for i in range(100):
            t = tuple(sorted(random.sample(letters_drawn,k=j)))
            if t in d:
                guesses_AI.append(d.get(t))
    
    if len(guesses_AI) != 0:            
        print("\nCould you have done better? Here is what i found: ")    
        # for guess in guesses_AI:
            # print(",".join(guess))
        best = max((w for g in guesses_AI for w in g), key=len)
        print("Longest better word:", best, f"(with {len(best)} letters)")
    
    else:
        print("Couldn't find anything better!")
    
    return score
    
def save_highscores(scores: list[tuple[str, int]], filename="highscores.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(scores, f)
        
def try_add_highscore(score: int, filename="highscores.pkl", limit=10):
    scores = load_highscores(filename)

    # If fewer than limit scores or score beats the worst
    if len(scores) < limit or score > min(s[1] for s in scores):
        name = input("New highscore! Enter your name: ").strip()
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        scores.append((name, score, timestamp))
        scores.sort(key=lambda x: x[1], reverse=True)

        scores = scores[:limit]

        save_highscores(scores, filename)
        print("Highscore added!\n")
    else:
        print("Nice try! But not quite a highscore.")
        
def display_highscores():
    scores = load_highscores()
    print("\n🏆 Highscores:")
    for i, (name, score, date) in enumerate(scores, start=1):
        print(f"{i:>2}. {name:<12} {score:>3} pts  ({date})")
    
# global variables ------------------------------------------------------------

# letters with bias towards more common letters
letter_pool = (
     "eeeeeaaaaiiiiioooonnnnrrrrttttllllssuuudddgg" 
     "bbccmmppffhhvvwwyykjxqz"
)

vowels = "aeiou"

# loading the dictionary
d = load_anagram_dict('anagrams.pkl')


# actual game -----------------------------------------------------------------

while True:
    clear_screen()    
    print('Welcome to CountDown the game!\n'+'-'*30+'\n')
    print("In each round 11 letters are drawn at random in each of the three"
          "rounds. Try to find words that are as long as possible.\n")
    
    total_score = 0
    
    rounds = 3
    
    for i in range(rounds):
        print('\nRound',i+1,":\n"+"-"*30)
        total_score += play_round()       
    
    print("\nTotal Score:",total_score,"point(s)\n")
    
    # hall of fame
    try_add_highscore(total_score)
    display_highscores()
    
    choice = input("Play again? (y/n): ").strip().lower()
    
    if choice != 'y':
        break