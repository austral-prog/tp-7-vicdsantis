def index_of_by_index(word, lista, indexx):
    for index, element in enumerate(lista[indexx:], indexx):
        if element == word:
            return index
    return -1
def index_of_empty(lista):
    for index, element in enumerate(lista):
        if element == "":
            return index
    return -1
def index_of(word, lista):
    for index, element in enumerate(lista):
        if element == word:
            return index
    return -1
def put(word, lista):
    for index, element in enumerate(lista):
        if element == "":
            lista[index] = word
            return index
    return -1

def remove(word, lista):
    count = 0
    for index, element in enumerate(lista):
        if element == word:
            lista[index] = ""
            count += 1
    return count
