from database import *
import string
from random import *
from datetime import *
from tkinter import *


def idfinder():
    cur.execute('select * from bericht order by bericht_id asc')
    con.commit()
    id = 1
    for n in cur.fetchall():
        while id == n[0]:
            id = id + 1
    return id


def stationlijst():
    file = open("Spoorlijst.txt")
    lijst = file.readlines()
    file.close()

    stationlijst = []
    for n in range(0, len(lijst)):
        noenter = lijst[n].strip("\n")
        stationlijst.append(noenter)

    return stationlijst
