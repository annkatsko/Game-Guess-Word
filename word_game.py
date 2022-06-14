from random import choice
from csv import reader


with open('word_game.csv', encoding='utf-8') as r_file:
    file_reader = reader(r_file, delimiter=',')
    d = {row[0]: row[1] for row in file_reader}


def main():
    game = True
    while game:
        computer_word = choice(list(d))
        hidden_word = '*' * len(computer_word)
        attempts = 5
        print(f'Computer guessed some word -> {hidden_word}.'
              f'\nYou should guess this word by typing a letter. '
              f'\nHere is help sentence: {d[computer_word]}.'
              f'\nYou have {attempts} attempts.'
              f'\n')
        while True:
            letter = str(input('Type your letter -> '))
            if check_for_right_input(letter):
                if letter.lower() in computer_word:
                    indexes = [i for i, val in enumerate(computer_word) if val == letter.lower()]
                    for index in indexes:
                        hidden_word = hidden_word[:index] + letter.lower() + hidden_word[index+1:]
                    print(f'Letter "{letter}" is in word -> {hidden_word}')
                else:
                    print(f'Letter "{letter}" is not in the word {hidden_word}')
                    attempts -= 1
                    print(f'Attempts left: {attempts}')
                if hidden_word == computer_word:
                    print(f'You won! The word was "{computer_word}"')
                    break
                if attempts == 0:
                    print(f'Game over. The word was "{computer_word}"')
                    break
        game = new_game()


def new_game():
    user_answer = input('Would you like to play once again? Type "Yes" or "No" -> ').lower()
    if user_answer == 'no':
        print('You have comleted the game!')
        return False
    elif user_answer == 'yes':
        return True
    else:
        print('Command is not correct, repeat, please')


def check_for_right_input(user_input):
    if not user_input.isalpha():
        print('You should type only a letter')
        return False
    elif len(user_input) > 1:
        print('You should type only one letter')
        return False
    else:
        return True


main()
