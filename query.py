from bsddb3 import db

database = db.DB()
DB_File = 'em.idx'
database.open(DB_File, None, db.DB_BTREE, db.DB_CREATE)

curs = database.cursor()

iter = curs.first()

while iter:
    print(iter)
    iter = curs.next()

