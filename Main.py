from Boggle import load_lexicon, createBoard, printBoard, tokenize, findBreak, find_on_board
from Boggle_AI import build_words, rec_build_a_word
import webbrowser, time
from multiprocessing import Pool as ThreadPool

def main():
    print("Welcome to my game of boggle. Wait 8 seconds at the end for a surprise! :)")
    time.sleep(4)
    print("You've got 3 minutes to find as many words as you can")
    score_card = 0
    used_words = []
    lexicon = load_lexicon()
    board = createBoard()
    #pool = ThreadPool(13)
    #total = pool.apply(build_words, board, lexicon)
    total = build_words(board,lexicon)
    start = time.time()
    while True:
        printBoard(board)
        player_word = input('Whats the good word? ').lower()
        if (time.time() - start) > 180:
            print("Sorry, you ran out of time. Go faster next time")
            time.sleep(4)
            break
        if player_word == '/quit':
            break
        if player_word in used_words:
            print("Sorry, the word is already used")
            continue
        if len(player_word) <= 2:
            print("Sorry, your word should be 3 letters or more")
            continue
        tokens, is_valid = tokenize(player_word)
        if is_valid:
            is_valid = find_on_board(board, player_word)
            if is_valid:
                is_valid = findBreak(lexicon, player_word)
                if is_valid:
                    used_words.append(player_word)
                    if len(player_word) <= 4:
                        print('Nailed it! You get one point!')
                        score_card += 1
                    elif len(player_word) == 5:
                        print('Awesome! Take two points!')
                        score_card += 2
                    elif len(player_word) == 6:
                        print("Wow! You've earned yourself three points!")
                        score_card += 3
                    elif len(player_word) == 7:
                        print("Holy cow! How'd you manage that? Take these five points! You've earned them!")
                        score_card += 5
                    else:
                        print("Okay, you must be cheating. Take these probably-ill-earned eleven points, you dirty trick.")
                        score_card += 11
                else:
                    print('Not in the lexicon, sorry :(')
            else:
                print('Sorry, the word was not on the board XP')
        else:
            print('Failed to tokenize: please contact tech support O_O')
    pool.close()
    pool.join()
    print("Nice job! Here's your total score:", score_card)
    print("Here are all of the words that you used: ", used_words)
    missed = [x for x in total if x not in used_words]
    print("Here's all of the words that you didn't find: ", missed)
    miss_score =0
    for poss in missed:
        if len(poss) <= 4:
            miss_score += 1
        elif len(poss) == 5:
            miss_score += 2
        elif len(poss) == 6:
            miss_score += 3
        elif len(poss) == 7:
            miss_score += 5
        else:
            miss_score += 11
    print("Here's the amount that you could've gotten: ", miss_score)
    time.sleep(5)
    print("Here's a video of a Genji meme: ")
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=wz6w7qzOxXs", new=0, autoraise=True)
if __name__ == "__main__":
    main()