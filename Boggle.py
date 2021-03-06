from random import randint, shuffle
from arrayutils import arrayCopy, arrayCheck
from BinarySearch import findBreak, breakArray

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
def load_lexicon():
    with open("twl06.txt") as f:
        lexicon = f.read().splitlines()
        return lexicon
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
            tokens.append(word_char.lower())
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

def rec_find_on_board(board, tokens, visited, possibles):
    word_idx = len(visited)
    if word_idx == len(tokens):
        return True
    word_token = tokens[word_idx]
    for board_idx in possibles:
        board_token = board[board_idx].lower()
        if word_token == board_token and not arrayCheck(visited, board_idx):
            nex_vis = arrayCopy(visited)
            nex_vis.append(board_idx)
            nex_pos = compute_next_possibles(board_idx)
            found = rec_find_on_board(board, tokens, nex_vis, nex_pos)
            if found:
                return True

    return False

def compute_next_possibles(cur_idx):
    possibles = []
    if cur_idx % 4 == 0:
        possibles = [cur_idx - 4, cur_idx + 4,
                     cur_idx - 3, cur_idx + 1, cur_idx + 5]

    elif cur_idx % 4 == 3:
        possibles = [cur_idx - 4, cur_idx + 4,
                     cur_idx - 5, cur_idx - 1, cur_idx + 3]

    else:
        possibles = [cur_idx - 4, cur_idx + 4,
                     cur_idx - 5, cur_idx - 1, cur_idx + 3,
                     cur_idx - 3, cur_idx + 1, cur_idx + 5]
    filtered_possibles = []

    for cur_idx in possibles:
        if cur_idx >= 0 and cur_idx < 16:
            filtered_possibles.append(cur_idx)

    return filtered_possibles

def find_on_board(board, tokens):
    return rec_find_on_board(board, tokens, [], [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
