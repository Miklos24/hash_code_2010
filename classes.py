'''
    Classes to assist in solving the problem.
'''

class Library:
    '''
        Class to hold a library object.

        variables:
        - id: name of the input file
        - books: a list of all books available to Library
        - b_scanned: a list of all books Library has scanned
        - su_time: the amount of time it takes Library to sign up
        - b_per_day: the number of books that Library can scan per day
        - tot_score: the sum of the scores of all books in Library
    '''
    def __init__(self, id, time, b):
        self.id = id
        self.books = []
        self.b_scanned = []
        self.su_time = time
        self.b_per_day = b
        self.tot_score = 0
