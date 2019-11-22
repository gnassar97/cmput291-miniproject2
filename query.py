from bsddb3 import db

#database = db.DB()
#B_File = 'em.idx'
#database.open(DB_File, None, db.DB_BTREE, db.DB_CREATE)

def options_interface():
    display_options()
    option = int(input("option: "))

    while option != 0:

        if option < 0 or option > 10:
            print("INVALID OPTION, try again")

        else:
            queries.get(option)()
            display_options()

        option = int(input("option: "))
    


def emails_with_subject():
    pass

def emails_with_subject_and_body():
    pass

def emails_with_prefix():
    pass

def emails_from():
    pass

def emails_to():
    pass

def emails_with_to_and_to():
    pass

def emails_on_date():
    pass

def emails_after_date():
    pass

def emails_with_bcc_cc():
    pass

def emails_with_terms_and_date():
    pass


def display_options():
    print("Select one of the following queries to proccess (0 to exit)")
    print("1 Email with subject")
    print("2 email with subject and body")
    print("3 email with prefix")
    print("4 email from")
    print("5 email to")
    print("6 email with two recipients")
    print("7 email on date")
    print("8 email after date")
    print("9 email with bcc and cc")
    print("10 email with term and before date")

queries = {1:emails_with_subject, 2:emails_with_subject_and_body, 3:emails_with_prefix, 4:emails_from, 5:emails_to, 
           6:emails_with_to_and_to, 7:emails_on_date, 8:emails_after_date, 9:emails_with_bcc_cc, 10:emails_with_terms_and_date}

options_interface()