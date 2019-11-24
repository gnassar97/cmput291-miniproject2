from bsddb3 import db

#database = db.DB()
#DB_File = 'em.idx'
#database.open(DB_File, None, db.DB_BTREE, db.DB_CREATE)

em_file = './index/em.idx'
da_file = './index/da.idx'
te_file = './index/te.idx'
re_file = './index/re.idx'

def user_interface():
    user_input()
    



def parse():
	data = re.split("(:|\s|>=|<=|>|<)", string)
    data.append('')
    # initialize a list to take in all the arguments by type
    # to be appended to
    prefixList = []
    colonDict = defaultdict(list)
    dateRangeDict = defaultdict(list)
    success = True
    activeColon = False
    potentialKey = ""

    # iterate through the query tokens and gather them by
    # their operator type for variables to be used in the
    # physical query of the database
    for i in range(len(data)):

        if(data[i] != "" and data[i] != " " and data[i] != ":" and data[i] != "<" and data[i] != "<=" and data[i] != ">" and data[i] != ">="):
            potentialKey = data[i]

        if "%" in data[i]:
            activeColon = False
            if data[i][-1:] == "%":
                # If something doesn't exist before %, error
                # or if percent is not at the end of the segment, error
                prefix = data[i][:-1]

def queries():
	database = db.DB()
    database.set_flags(db.DB_DUP)
    database.open("te.idx", None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    # create temporary table for the currently valid rows to be intersected with, must be cleared after each of the
    # following for loops
    temp = []
    # Iterate through query requirments and find rows which satisfy all of them
    # starting with subject terms
    if(colDict["subj"]):
        for i in colDict["subj"]:
            key = ("s-" + i).encode()
            row = database.get(key)
            if(row):
                #print(row.decode('utf-8'))
                temp.append(row.decode('utf-8'))
        validRows.append(temp)

    temp = []
    if(colDict["body"]):
        for i in colDict["body"]:
            key = ("b-" + i).encode()
            row = database.get(key)
            if(row):
                #print(row.decode('utf-8'))
                temp.append(row.decode('utf-8'))
        validRows.append(temp)

    temp = []


def user_input():
    full_or_brief = input("Would you like the output to be full or brief? (output=full or output=brief)")

