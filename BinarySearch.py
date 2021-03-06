def findBreak(array, word):
    return breakArray(array, word, 0, len(array))
def breakArray(array, check, start, end):
    if end == start:
        return False
    mid = start + int((end-start) / 2)
    wordup = array[mid]
    if wordup == check:
        return True
    elif wordup < check:
        return breakArray(array, check, mid+1, end)
    else:
        return breakArray(array, check, start, mid)
def main():
    if __name__ == "__name__":
        with open("twl06.txt") as f:
            lexicon = f.read().splitlines()
        print(findBreak(lexicon, 'goo'))


main()