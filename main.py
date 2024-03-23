import random

# import hangmanwords
# chosen_word = random.choice(hangmanwords.word_list)

from hangmanart import word_list

chosen_word = random.choice(word_list)
lives = 6

from hangmanart import logo

print(logo)
print(chosen_word)
display = []
# for letter in chosen_word:
#     display += "_"
# print(display)
for _ in range(len(chosen_word)):  # range from 0 to the number of leter in chossen word
    display += "_"


end_of_game = False  # using bollean type
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"you've already gueesd {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
    if lives == 0:
        end_of_game = True
        print("you loose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("you win")
    from hangmanart import stages

    print(stages[lives])
