print("************ sobhani *Exercie3* Data-Mining ************")

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Exercise Data Mining Marzieh Sobhani Mr VafaeeJahan class Data Mining'))

print("************ sobhani *Exercie3* Data-Mining ************")