import psycopg2

con = psycopg2.connect(  # Connect met de database
    host='localhost',  # De host waarop je database runt
    database='proja_nsconsumentenzuil2',  # Database naam
    user='postgres',  # Als wat voor gebruiker je connect, standaard postgres als je niets veranderd
    password='TjonANjoek180501',  # Wachtwoord die je op hebt geven bij installatie
    port=5433  # runt standaard op port 5432. Bij installatie andere port gebruikt? Port-command is vereist
)
cur = con.cursor()  # Cursor is gecreeëerd (wordt uitgelegd bij Modelling)
