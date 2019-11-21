import os

def sort_files():
    os.system('sort -u -o terms.txt terms.txt')
    os.system('sort -u -o emails.txt emails.txt')
    os.system('sort -u -o dates.txt dates.txt')


def create_date_index():
    os.system('sh load-dates.sh')

def create_terms_index():
    os.system('sh load-terms.sh')


def create_terms_index():
    os.system('sh load-emails.sh')


sort_files()

create_date_index()

create_terms_index()