def arrayCopy(ori):
    copy = []
    for i in ori:
        copy.append(i)
    return copy

def arrayCheck(copy, answ_sheet):
    validation = False
    for char in copy:
        if char == answ_sheet:
            validation = True
            print("Correct! Monika is so proud of you!")
            return True

    print("This is the wrong word, try again")
    return False


def main():
    if __name__ == "__name__":
        cardi = 'D'
        ori = ['C','A','P']
        hash = arrayCopy(ori)
        arrayCheck(hash, cardi)