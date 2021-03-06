import random
print("H A N G M A N")
print()
# selecting a word
answers_list = ['python', 'java', 'kotlin', 'javascript']
x = random.choice(answers_list)
# starting to guess
guess_form = list('-' * (len(x)))
hint = "".join(guess_form)
guessed_letters = list()
attempts = 0
menu = input('Type "play" to play the game, "exit" to quit:')
while menu == 'play' and menu != 'exit':
    while attempts < 8 and hint != x:
        print()
        print(hint)
        answer = input("Input a letter: ")
        if len(answer) > 1:
            print("You should input a single letter")
        elif answer.isalpha() is False or answer.islower() is False:
            print("Please enter a lowercase English letter")
        elif answer in guessed_letters:
            print("You've already guessed this letter")
        else:
            guessed_letters.append(answer)
            if answer in set(x):
                letter_position = int(x.find(answer))
                if x.count(answer) == 2:
                    rletter_position = int(x.rfind(answer))
                    del guess_form[letter_position]
                    del guess_form[rletter_position - 1]
                    guess_form.insert(letter_position, answer)
                    guess_form.insert(rletter_position, answer)
                    hint = "".join(guess_form)
                    print()
                else:
                    del guess_form[letter_position]
                    guess_form.insert(letter_position, answer)
                    hint = "".join(guess_form)
                    print()
            else:
                print("That letter doesn't appear in the word")
                attempts += 1
    else:
        if attempts > 8:
            print("You lost!")
            menu = input('\nType "play" to play the game, "exit" to quit:')
        else:
            print(hint)
            print('''You guessed the word {}!
    You survived!'''.format(x))
            menu = input('\nType "play" to play the game, "exit" to quit:')
else:
    menu = input('\nType "play" to play the game, "exit" to quit:')