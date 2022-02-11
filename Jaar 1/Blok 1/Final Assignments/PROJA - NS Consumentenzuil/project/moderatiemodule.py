from database import *


def admincache():
    admin = []
    admin.clear()
    cur.execute('select * from moderator')
    con.commit()
    data = cur.fetchall()
    for n in data:
        admin.append(n)
    return admin
