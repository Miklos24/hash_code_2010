'''
    Functions to assist with scoring a given solution.

    For main:
    - commandline arg 1: data file name
    - commandline arg 2: output file name

    Example usage:
    "python3 scorer.py data/a_example.txt out/a_out_224101"
'''

import sys
from classes import Library
from fileIO import readFile

def readOutFile(f_data, f_out):
    '''
        Function to read the output file and class lists (optional).

        arguments:
        - f_data: name of the data file corresponding to a given output file
        - f_out: name of the output file

        returns:
        - books: dictionary that describes book scores (id -> scores)
        - libraries: list of Library objects with the order/data given in
          output file
    '''
    books, libraries, num_d = readFile(f_data)
    sorted_libraries = []
    with open(f_out) as f:
        num_l = [int(x) for x in next(f).split()][0]
        for _ in range(num_l):
            id, num_b = [int(x) for x in next(f).split()]
            libraries[id].b_scanned = [int(x) for x in next(f).split()]
            sorted_libraries.append(libraries[id])
    return books, sorted_libraries

def score(books, libraries):
    '''
        Function to calculate the score.

        arguments:
        - books: dictionary that describes book scores (id -> scores)
        - libraries: list of Library objects, sorted by sign up order

        returns:
        - score: integer total score for solution
    '''
    scanned = set()
    score = 0
    for l in libraries:
        for b in l.b_scanned:
            if b not in scanned:
                score += books[b]
                scanned.add(b)
    return score

if __name__ == "__main__":
    books, libraries = readOutFile(sys.argv[1], sys.argv[2])
    print(score(books, libraries))
