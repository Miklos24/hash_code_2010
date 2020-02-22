'''
    Functions to read input file and write output file.
'''
import time
from classes import Library

def readFile(fName):
    '''
        Function to read the input file.

        arguments:
        - fName: name of the input file.

        returns:
        - books: a dictionary of books that maps from id -> score
        - libraries: a list of Library objects
        - num_d: the number of days in the simulation
    '''
    with open(fName, 'r') as f:
        num_b, num_l, num_d = [int(x) for x in next(f).split()]
        books = dict()
        book_list = [int(x) for x in next(f).split()]
        for i, x in enumerate(book_list):
            books[i] = int(x)

        libraries = []
        for i in range(num_l):
            b, days, b_per_day = [int(x) for x in next(f).split()]
            libraries.append(Library(i, days, b_per_day))
            libraries[i].books = [int(x) for x in next(f).split()]

    return books, libraries, num_d

def outputFile(fName, libraries):
    '''
        Function to produce the output file.

        arguments:
        - fName: name of the output file.
        - libraries: a list of libraries sorted by sign-up order

        returns: None
    '''
    with open("out/" + fName[5] + "_out_" + time.strftime("%H%M%S") + ".txt", 'w') as f:
        used_libaries = sum(1 for l in libraries if len(l.b_scanned) != 0)
        f.write(str(used_libaries) + "\n")
        for l in libraries:
            if len(l.b_scanned) != 0:
                f.write(str(l.id) + " " + str(len(l.b_scanned)) + "\n")
                f.write(' '.join([str(x) for x in l.b_scanned]) + "\n")
        f.close()
