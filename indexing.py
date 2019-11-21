import os

def sort_files():
    os.system('sort -u -o terms.txt terms.txt')
    os.system('sort -u -o emails.txt emails.txt')
    os.system('sort -u -o dates.txt dates.txt')


def create_date_index():
    os.system('sh ./scripts/load-dates.sh')

def create_terms_index():
    os.system('sh ./scripts/load-terms.sh')


def create_emails_index():
    os.system('sh ./scripts/load-emails.sh')


sort_files()

create_date_index()

create_emails_index()

create_terms_index()