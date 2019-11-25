import os
import sys

def sort_files():
    os.system('sort -u -o ./parsed/terms.txt ./parsed/terms.txt')
    os.system('sort -u -o ./parsed/emails.txt ./parsed/emails.txt')
    os.system('sort -u -o ./parsed/dates.txt ./parsed/dates.txt')
    os.system('sort -u -o ./parsed/recs.txt ./parsed/recs.txt')

def create_date_index():
    os.system('sh ./scripts/load-dates.sh')

def create_terms_index():
    os.system('sh ./scripts/load-terms.sh')


def create_emails_index():
    os.system('sh ./scripts/load-emails.sh')

def create_records_index():
    os.system('sh ./scripts/load-records.sh')

def create_idx_files():
    sort_files()
    create_date_index()
    create_emails_index()
    create_terms_index()
    create_records_index()