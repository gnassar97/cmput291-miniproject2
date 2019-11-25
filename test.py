from bsddb3 import db
import re

em_file = './index/em.idx'
da_file = './index/da.idx'
te_file = './index/te.idx'
re_file = './index/re.idx'

queries = [

    r'\s*subj\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*body\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*from\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*to\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*bcc\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*cc\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*output\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*date\s*[\>=\<=\>\<\:](?:(?!body|to|from|bcc|cc|output|subj).)*',

]

query = input()

to_proccess = []
wildcards = []

query = re.sub("\s\s+" , " ", query)

for regex in queries:
    match = re.findall(regex, query)
    if match:
        try:
            test =  re.split("(:|>=|<=|>|<)", match[0])
            keyword = test[0]
            values = test[2]
            #keyword = match[0].split(':')[0]
            #values = match[0].split(':')[1]
            value = values.split()[0]
            to_proccess.append([keyword,value])
            wildcard = values.split()
            #print(values)
            operator = test[1]

            for i in range(1,len(wildcard)):
                wildcards.append(wildcard[i])
            print(wildcard)

        except:
            proccess =  re.split("(:|>=|<=|>|<|=)", match[0])
            #proccess = match[0].split('>')
            keyword = proccess[0]
            value = proccess[2]
            to_proccess.append([keyword, value])          
            operator = proccess[1]

print(to_proccess)
print(wildcards)

def main():
    terms = db.DB()
    terms.open(te_file, None, db.DB_BTREE, db.DB_CREATE)
    
    emails = db.DB()
    emails.open(em_file, None, db.DB_BTREE, db.DB_CREATE)

    dates = db.DB
    dates.open(da_file, None, db.DB_BTREE, db.DB_CREATE)

    recs = db.DB
    recs.open(re_file, None, db.DB_HASH, db.DB_CREATE)

    
    
    row_id = []
    for i in range(0, len(to_proccess)):
        if to_proccess[0] == "subj":  
            subj_rows = []               
            curs = terms.cursor()
            key = "s-" + i[1]
            result = curs.set(key.encode("utf-8"))
            if result == None:
                return
            else:
                subj_rows.append(result[1])
            result = curs.next_dup()

            while result != None:
                subj_rows.append(result[1])
                result = curs.next_dup()

        if to_proccess[0] == "body":
            body_rows = []
            curs = terms.cursor()
            key = "b-" + i[1]
            result = curs.set(key.encode("utf-8"))
            if result == None:
                return
            else:
                body_rows.append(result[1])
            result = curs.next_dup()

            while result != None:
                body_rows.append(result[1])
                result = curs.next_dup()


        if to_proccess[0] == "from":
            curs = emails.cursor()
            key = "from-" + i[1]
            result = curs.set(key.encode("utf-8"))
            if result == None:
                return
            else:
                row_id.append(result[1])
            result = curs.next_dup()

            while result != None:
                row_id.append(result[1])
                result = curs.next_dup() 

        if to_proccess[0] == "to":
            curs = emails.cursor()
            key = "to-" + i[1]
            result = curs.set(key.encode("utf-8"))
            if result == None:
                return
            else:
                row_id.append(result[1])
            result = curs.next_dup()

            while result != None:
                row_id.append(result[1])
                result = curs.next_dup() 

        if to_proccess[0] == "bcc":
            curs = emails.cursor()
            key = "bcc-" + i[1]
            result = curs.set(key.encode("utf-8"))
            if result == None:
                return
            else:
                row_id.append(result[1])
            result = curs.next_dup()

            while result != None:
                row_id.append(result[1])
                result = curs.next_dup() 

        if to_proccess[0] == "cc":
            curs = emails.cursor()
            key = "cc-" + i[1]
            result = curs.set(key.encode("utf-8"))
            if result == None:
                return
            else:
                row_id.append(result[1])
            result = curs.next_dup()

            while result != None:
                row_id.append(result[1])
                result = curs.next_dup() 

    row_id.append(intersection(subj_rows, body_rows))
    print(row_id)



  








main()