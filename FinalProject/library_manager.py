import csv
import os

DATA_FILE = "library_books.csv"

def load_blocks():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "author", "isbn", "status"])
            return []
def save_books(books):
    pass