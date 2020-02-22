'''
    Functions to generate a solution output file.

    For main:
    - commandline arg 1: data file name

    Example usage:
    "python3 solution.py data/a_example.txt"

'''

from classes import Library
from fileIO import readFile, outputFile
from scorer import score
import sys

def reward_func(l, k_s, k_p, k_t) :
    '''
        Function to calculate reward for a library for use in greedy algorithm.
        This takes a series of constants, which have been tuned for each dataset.

        arguments:
        - l: the library in question
        - k_s: magic score constant
        - k_p: magic scanning speed constant
        - k_t: magic sign-up speed constant

        returns:
        - (integer) reward value
    '''
    return (k_t * l.su_time) - (k_s * l.tot_score + k_p * l.b_per_day)

def scan_books(books, libraries, num_days):
    '''
        Function to read the scan books from each library. It begins by sorting
        each libary's books by max score value, and then calculates how many
        books can be scanned given that library's rate of scanning. It then adds
        those books to the library's list of scanned books, given that that
        particular book hasn't been scanned yet.

        arguments:
        - books: a dictionary of books that maps from id -> score
        - libraries: a list of Library objects
        - num_days: the number of days in the simulation

        returns:
        - libraries: a list of Library objects with scanned books updated

    '''
    start_day = 0
    scanned_books = set()
    for l in libraries:
        #sort books by maximum score
        l.books.sort(key=lambda x : books[x])

        #calculate when the library starts scanning & how many days it may scan
        start_day += l.su_time
        if start_day > num_days:
            break
        time_to_scan = num_days - start_day
        books_to_be_scanned = time_to_scan * l.b_per_day

        #scan as many books as possible
        i = 0
        for _ in range(books_to_be_scanned):
            if l.books == []:
                break
            book = l.books.pop()
            #if the chosen book has already been scanned, don't scan it
            while book in scanned_books and l.books != []:
                book = l.books.pop()
            scanned_books.add(book)
            l.b_scanned.append(book)
    return libraries

def sort_by_diff(libraries):
    '''
        This function sorts the libraries based off minimum intersection between
        consecutive libraries. In other words, it tries to minimize the number
        of duplicate books between consecutive libraries.

        (NOTE - We later realized that this is a suboptimal way to approach
        this problem. We should have been minimizing duplicates among ALL
        libraries, not just consecutive.)

        arguments:
        - libraries: list of library objects

        returns:
        - libraries: list of library objects with minimized overlap

    '''
    libraries.sort(key=lambda l : len(l.books))
    libraries.reverse()

    for i in range(len(libraries) - 1):
        max_diff = 0
        max_idx = i + 1
        for j in range(i + 1, len(libraries)):
            diff = len(set(libraries[j].books) - set(libraries[i].books))
            if diff > max_diff:
                max_diff = diff
                max_idx = j
            if diff == len(libraries[j].books):
                break
        libraries[i + 1], libraries[max_idx] = libraries[max_idx], libraries[i + 1]

    return libraries

def main():
    books, libraries, num_days = readFile(sys.argv[1])
    for l in libraries:
        l.tot_score = sum(books[b] for b in l.books)

    file_id = sys.argv[1][5]
    if file_id == 'a'or file_id == 'b':
        libraries.sort(key=lambda x : x.su_time)
    elif file_id == 'c':
        libraries.sort(key=lambda x : reward_func(x, 1, 0, 34))
    elif file_id == 'd':
        libraries = sort_by_diff(libraries)
    elif file_id == 'e':
        libraries.sort(key=lambda x : reward_func(x, 1, 45900, 45900))
    elif file_id == 'f':
        libraries.sort(key=lambda x : reward_func(x, 1, 7000, 7000))

    libraries = scan_books(books, libraries, num_days)
    outputFile(sys.argv[1], libraries)
    print(score(books, libraries))

if __name__ == "__main__":
    main()
