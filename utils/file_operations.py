from flashcard import Flashcard


def read_flashcards_from(file_path):
    flashcards = []
    with open(file_path, "r") as vocab:
        for line in vocab:
            info = line.split()
            flashcard = Flashcard(info[0].strip('"'), info[1].strip('"'))
            flashcards.append(flashcard)
    return flashcards
