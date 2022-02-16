import string
from tkinter.messagebox import showinfo
from random import *
from datetime import *
from database import *
from reactiemodule import *


def opvulling():  # maakt n berichten aan voor demonstratie opvulling
    for n in range(0, 500):
        ber_id = idfinder()
        naam = ''.join(sample((string.ascii_lowercase + string.digits) * 16, 16))
        station = randint(1, len(stationlijst()))
        gekeurd = randint(0, 2)
        if gekeurd == 0:
            status = 'approved'
        elif gekeurd == 1:
            status = 'rejected'
        else:
            status = 'pending'
        char_set = string.ascii_lowercase + string.digits
        bericht = ''.join(sample(char_set * 140, 140))
        datum = datetime.now().strftime("%b %d %Y")
        tijd = datetime.now().strftime("%H:%M:%S")
        cur.execute(
            'insert into bericht (bericht_id, naam, stat_id, bericht, status, datum, tijd) values (%s, %s, %s, %s, '
            '%s, %s, %s)',
            (ber_id, naam, station, bericht, status, datum, tijd))
        print(
            f"Bericht \033[1m{ber_id}\033[0m op station \033[1m{station}\033[0m bevat \033[1m{bericht}\033[0m is \033[1m{status}\033[0m en opgeslagen op \033[1m{datum}\033[0m, \033[1m{tijd}\033[0m")
        con.commit()


def deleteall():
    # Data Delete
    cur.execute('drop table bericht cascade ')
    con.commit()
    cur.execute('drop table moderator cascade')
    con.commit()
    cur.execute('drop table station cascade')

    # Data Create
    cur.execute('create table bericht (bericht_id integer primary key not null,naam varchar(32), stat_id integer, bericht varchar(140) not null, mod_id integer, status varchar(32) not null, datum date not null, tijd time not null);')
    con.commit()
    cur.execute('create table moderator (mod_id serial primary key not null, naam varchar(16) not null, wachtwoord varchar(16) not null);')
    con.commit()
    cur.execute('create table station (stat_id serial primary key not null, naam varchar(256), adres varchar(128), plaats varchar(128));')
    con.commit()
    cur.execute('ALTER TABLE bericht ADD CONSTRAINT bericht_mod_id_fk FOREIGN KEY (mod_id) REFERENCES moderator(mod_id);')
    con.commit()
    cur.execute('ALTER TABLE bericht ADD CONSTRAINT bericht_stat_id_fk FOREIGN KEY (stat_id) REFERENCES station(stat_id);')
    con.commit()
    cur.execute('insert into moderator(naam, wachtwoord) values (\'admin\', \'admin\');')
    for station in stationlijst():
        cur.execute('insert into station(naam) values (%s)', (station,))
        con.commit()
    print('\n\tAll data has been erased')


def deletefalse():
    cur.execute('delete from bericht where status = \'rejected\'')
    con.commit()
    print('\n\tCases \'rejected\' have been erased')
