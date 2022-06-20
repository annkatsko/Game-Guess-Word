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
        attempts = 0
        total_attempts = 5
        print(f'Computer guessed some word -> {hidden_word}.'
              f'\nYou should guess this word by typing a letter. '
              f'\nHere is help sentence: {d[computer_word]}.'
              f'\nYou have {total_attempts} attempts.'
              f'\n'
              f'You can guess hall word. If you want, type "#"')
        while True:
            letter = str(input('Type your letter -> '))
            if letter == '#':
                flag = True
                while attempts != total_attempts:
                    hall_word = str(input('Type your word or "back", if you want to guess a letter again -> '))
                    if hall_word == 'back':
                        print(f'Attempts left: {total_attempts - attempts}')
                        letter = str(input('Type your letter -> '))
                        break
                    flag = check_hall_word(hall_word, computer_word)
                    if flag:
                        print(f'You won!')
                        break
                    else:
                        attempts += 1
                        print(f'Attempts left: {total_attempts - attempts}')
                        continue
                else:
                    break
                if flag:
                    break
            if check_for_right_input(letter):
                if letter.lower() in hidden_word:
                    print(f'You have already guessed the letter "{letter} -> {hidden_word}"')
                    continue
                if letter.lower() in computer_word:
                    indexes = [i for i, val in enumerate(computer_word) if val == letter.lower()]
                    for index in indexes:
                        hidden_word = hidden_word[:index] + letter.lower() + hidden_word[index+1:]
                    print(f'Letter "{letter}" is in the word -> {hidden_word}'
                          f'\nKeep going!')
                else:
                    print(f'Letter "{letter}" is not in the word {hidden_word}')
                    attempts += 1
                    print(f'Attempts left: {total_attempts-attempts}')
                if attempts == total_attempts:
                    print(f'Round is over. The word was "{computer_word}"')
                    break
                if hidden_word == computer_word:
                    print(f'You won! The word was "{computer_word}"')
                    break
        game = repeat_game()


def repeat_game():
    user_answer = input('Would you like to play once again? Type "Yes" or "No" -> ').lower()
    while True:
        if user_answer == 'no':
            print('You have comleted the game!')
            return False
        elif user_answer == 'yes':
            return True
        else:
            print('Command is not correct, repeat, please')
            user_answer = input('Type correct answer ("Yes" or "No") -> ').lower()

def check_for_right_input(user_input):
    if not user_input.isalpha():
        print('You should type only a letter')
        return False
    elif len(user_input) > 1:
        print('You should type only one letter')
        return False
    else:
        return True

def check_hall_word(word, computer_word):
    if word.lower() == computer_word:
        return True
    else:
        print(f'No, a computer guessed the other word. Try again')
        return False


main()
