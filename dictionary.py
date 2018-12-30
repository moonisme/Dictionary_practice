import json
from difflib import get_close_matches

data = json.load(open('dict.json'))

def get_def(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input(f'Did you mean {get_close_matches(word, data.keys())[0]} instead? [y or n]: ')
        action = action.lower()
        if action == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif action == 'n':
            print("The word doesn't exist.")
        else:
            print('Incorrct commend, giving up.')


word_user = input('Enter a word: ')

output = get_def(word_user)
print()

if type(output) == list:
    count = 0
    for i in output:
        count +=1
        print(f'{count}. {i}')

