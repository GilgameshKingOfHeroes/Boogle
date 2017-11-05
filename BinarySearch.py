from arrayutils import arrayCopy, arrayCheck
import time

def findBreak(array, word):
    return breakArray(array, word, 0, len(array))
def breakArray(array, check, start, end):
    if end == start:
        print("Pixy, why u betray meh!?")
        return False
    mid = start + int((end-start) / 2)
    wordup = array[mid]
    if wordup == check:
        print("Yo buddy, you still alive?")
        return True
    elif wordup < check:
        return breakArray(array, check, mid+1, end)
    else:
        return breakArray(array, check, start, mid)

def main():
    with open("twl06.txt") as f:
        lexicon = f.read().splitlines()
    print(findBreak(lexicon, 'goo'))


main()