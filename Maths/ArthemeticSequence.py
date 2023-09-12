# sequence is a list of numbers which are in order with certain pattern's

def createSequence(progressionFunc, firstTerm, numberOfTerms):
    sequence = [firstTerm]
    for i in range(2, numberOfTerms + 1):
        sequence.append(progressionFunc(firstTerm, i))
    return sequence


# Arithmetic Progression in which each term is obtained by adding / Subtracting a fixed number to the preceding term
# except the first term.
def arithmeticProgressionExplicit(firstTerm, index):
    common_difference = 2
    return firstTerm + (common_difference * (index - 1))


def ap_recursive(firstTerm, totalTerms):
    sequence = [firstTerm]
    current_index = 2
    while current_index <= totalTerms:
        sequence.append(arithmeticProgressionExplicit(firstTerm, current_index))
        current_index += 1
    return sequence


if __name__ == '__main__':
    print(createSequence(arithmeticProgressionExplicit, 1, 10))
    print(ap_recursive(1, 10))
