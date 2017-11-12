def arrayCopy(ori):
    copy = []
    for i in ori:
        copy.append(i)
    return copy

def arrayCheck(array, word):
    validation = False
    for char in array:
        if char == word:
            validation = True
            return True
    return False


def main():
    if __name__ == "__name__":
        cardi = 'D'
        ori = ['C','A','P']
        hash = arrayCopy(ori)
        arrayCheck(hash, cardi)