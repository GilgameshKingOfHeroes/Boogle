from BinarySearch import findBreak, breakArray
from arrayutils import arrayCopy, arrayCheck
from Boggle import load_lexicon, rec_find_on_board, compute_next_possibles, createBoard, printBoard


def build_words(board, lexicon):
    found_words = []
    rec_build_a_word(board, lexicon, "", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [], found_words)
    return found_words

def rec_build_a_word(board, lexicon, word, next_dice, visited_dice, found_words):
    if len(word) >= 3 and findBreak(lexicon, word) and word not in found_words:
        found_words.append(word)
    for next_die in next_dice:
        token = board[next_die]
        next_word = word + token
        if next_die not in visited_dice:
            next_vis = arrayCopy(visited_dice)
            next_vis.append(next_dice)
            rec_build_a_word(board, lexicon, next_word, compute_next_possibles(next_die), next_vis, found_words)

def main():
    board = createBoard()
    lex = load_lexicon()
    printBoard(board)
    words = build_words(board, lex)
    print(words)

if __name__ == "__main__":
    main()