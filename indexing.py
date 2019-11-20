import os

def sortFiles():
    os.system('sort -u -o terms.txt terms.txt')
    os.system('sort -u -o emails.txt emails.txt')
    os.system('sort -u -o dates.txt dates.txt')


def create_date_index():
    os.system('sh load-dates.sh')


create_date_index()