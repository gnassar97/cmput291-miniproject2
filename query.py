from bsddb3 import db

#database = db.DB()
#DB_File = 'em.idx'
#database.open(DB_File, None, db.DB_BTREE, db.DB_CREATE)

em_file = './index/em.idx'
da_file = './index/da.idx'
te_file = './index/te.idx'
re_file = './index/re.idx'


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
    terms = db.DB()
    terms.open(te_file, None, db.DB_BTREE, db.DB_CREATE)
    curs = terms.cursor()
    
    term = str(input('Enter a term to search for in subject field: '))
    term = 'b-'+term

    result = curs.set(term.encode('utf-8'))

    matches = []

    if result == None:
        return

    else:
        matches.append(result[1])

    result = curs.next_dup()

    while result != None:
        matches.append(result[1])
        result = curs.next_dup()
    
    print(matches)


def emails_with_subject_and_body():
    pass

def emails_with_prefix():
    pass

def emails_from():
    email = str(input('Enter an email: '))
    get_email_records('from', email)

  
def emails_to():
    email = str(input('Enter an emial: '))
    get_email_records('to', email)

def emails_with_to_and_to():
    first_email = str(input("Enter first email: "))
    second_email = str(input("Enter second email: "))

    first_email = 'to-'+first_email
    second_email = 'to-'+second_email

    emails = db.DB()
    emails.open(em_file, None, db.DB_BTREE, db.DB_CREATE)
    curs1 = emails.cursor()
    curs2 = emails.cursor()

    result1 = curs1.set(first_email.encode('utf-8'))
    result2 = curs2.set(second_email.encode('utf-8'))

    matches = []

    while result1 != None and result2 != None:
        while result2 != None:
            if result2[1] == result1[1]:
                matches.append(result1[1])
            result2 = curs2.next_dup()
            
        result1 = curs1.next_dup()
        result2 = curs2.set(second_email.encode('utf-8'))
    

    records = db.DB()
    records.open(re_file, None, db.DB_HASH, db.DB_CREATE)
    curs = records.cursor()
    
    for i in range(0, len(matches)):
        row = str(matches[i].decode('utf-8'))
        result = curs.set(row.encode('utf-8'))
        rec_display = result[1].decode('utf-8')

        try:
            rec_display = rec_display.split('<subj>')[1]
            rec_display = rec_display.split('</subj>')[0]
            print(row + ' : ' + rec_display)

        except:
            print(row)



def emails_on_date():
    pass

def emails_after_date():
    pass

def emails_with_bcc_cc():
    pass

def emails_with_terms_and_date():
    pass


def get_email_records(emailType, email):
    emails = db.DB()
    emails.open(em_file, None, db.DB_BTREE, db.DB_CREATE)
    curs = emails.cursor()

    keys = []

    search = emailType+'-'+email

    result = curs.set(search.encode('utf-8'))

    if result == None:
        return

    else:
        keys.append(result[1])

    result = curs.next_dup()

    while result != None:
        keys.append(result[1])

        result = curs.next_dup()
    
    records = db.DB()
    records.open(re_file, None, db.DB_HASH, db.DB_CREATE)
    curs = records.cursor()

    for i in range(0, len(keys)):
        row = str(keys[i].decode('utf-8'))
        result = curs.set(row.encode('utf-8'))
        rec_display = result[1].decode('utf-8')

        try:
            rec_display = rec_display.split('<subj>')[1]
            rec_display = rec_display.split('</subj>')[0]
            print(row + ' : ' + rec_display)

        except:
            print(row)


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

