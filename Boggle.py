from random import randint, shuffle

DICE = [
    ['A','A','E','E','G','N'],
    ['A','B','B','J','O','O'],
    ['A','C','H','O','P','S'],
    ['A','F','F','K','P','S'],
    ['A','O','O','T','T','W'],
    ['C','I','M','O','T','U'],
    ['D','E','I','L','R','X'],
    ['D','E','L','R','V','Y'],
    ['D','I','S','T','T','Y'],
    ['E','E','G','H','N','W'],
    ['E','E','I','N','S','U'],
    ['E','H','R','T','V','W'],
    ['E','I','O','S','S','T'],
    ['E','L','R','T','T','Y'],
    ['H','I','M','N','U','Qu'],
    ['H','L','N','N','R','Z']
        ]

def tokenize(player_word):
    tokens = []
    is_valid = True
    word_idx = 0
    while word_idx < len(player_word):
        word_char = player_word[word_idx]
        word_idx += 1
        if word_char == 'q':
            if word_idx == len(player_word):
                is_valid = False
                break
            elif player_word[word_idx + 1] != 'u':
                is_valid = False
                break
            else:
                tokens.append('qu')
                word_idx +=1
        else:
            tokens.append(word_char.upper())
    return tokens, is_valid

def printBoard(board):
    count = 0
    line = ''
    for char in board:
        line += char
        count += 1
        if count < 4:
            if char == 'Qu':
                line += ' '
            else:
                line += '  '
        else:
            print(line)
            count = 0
            line = ''

def createBoard():
    board = []
    for die in DICE:
        idx = randint(0,5)
        face = die[idx]
        board.append(face)
    shuffle(board)
    return board

def main():
    board = createBoard()
    printBoard(board)
    player_word = input('Whats the good word? ')
    tokens, is_valid = tokenize(player_word)
    print(tokens)
main()