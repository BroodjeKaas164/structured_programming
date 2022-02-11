import tkinter
from tkinter import *
from reactiemodule import *
from moderatiemodule import *
from tkinter.messagebox import *
from sqlcontrol import *
import tweepy


# TODO station .lower functie gebruiken

class ReactieModule(Frame):  # Module | REACTIE
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.welkomscherm()

    def geefgebruikersnaamframe(self):
        self.welkomframe.pack_forget()
        self.gebruikersnaam()

    def geefreactieframe(self):
        self.gebruikframe.pack_forget()
        self.reactie()

    def geefwelkomframe(self):
        self.gebruikframe.pack_forget()
        self.reactieframe.pack_forget()
        self.welkomscherm()

    def welkomscherm(self):
        def gotomain():  # Return naar HOOFDMENU
            self.welkomframe.pack_forget()
            StartScherm()

        root.title('Welkom!')

        self.welkomframe = Frame(master=root, background='#f7d417')
        self.welkomframe.pack(fill='both', expand=True)

        self.welkomlabel = Label(master=self.welkomframe, text='Welkom bij NS!', foreground='#003373',
                                 font=('Sans', 16, 'bold'),  # bold, italic
                                 background='#f7d417', padx=10, pady=5)
        self.welkomlabel.pack(side=LEFT)

        self.welkombutton = Button(master=self.welkomframe, text='Continue', command=self.geefgebruikersnaamframe)
        self.welkombutton.pack(padx=10, pady=2, fill=X)

        self.cancel = Button(master=self.welkomframe, text='Cancel', foreground='red', command=gotomain)
        self.cancel.pack(padx=10, pady=2, fill=X)

    def gebruikersnaam(self):
        def gotomain():  # Return naar HOOFDMENU
            self.gebruikframe.pack_forget()
            StartScherm()

        root.title('Gebruikersnaam')

        self.gebruikframe = Frame(master=root, background='#f7d417')
        self.gebruikframe.pack(fill='both', expand=True)

        self.label = Label(master=self.gebruikframe, text='Geef een gebruikersnaam op.\nLeeg = \'Anoniem\'',
                           foreground='#003373', font=('Sans', 16, 'bold'),  # bold, italic
                           background='#f7d417', padx=10, pady=5)
        self.label.pack(side=LEFT)

        self.naaminvoer = Entry(master=self.gebruikframe)
        self.naaminvoer.pack(padx=10, pady=2, fill=X)

        self.startreaproc = Button(master=self.gebruikframe, text='Continue', command=self.geefreactieframe)
        self.startreaproc.pack(padx=10, pady=2, fill=X)

        self.back = Button(master=self.gebruikframe, text='Cancel', foreground='red', command=gotomain)
        self.back.pack(side='bottom', padx=10, pady=2, fill=X)

    def reactie(self):
        def gotomain():  # Return naar HOOFDMENU
            self.reactieframe.pack_forget()
            StartScherm()

        def identificatie(naam):
            if naam == '':
                naam = 'Anoniem'
            return naam

        def verificatie(station, bericht):
            if station != '':
                if station in stationlijst():
                    cur.execute('select stat_id from station where naam = %s', (station,)), con.commit()
                    return True
                else:
                    self.label['text'] = 'Station \"{}\" is niet geldig'.format(station)
                    return False
            elif station == '':
                self.label['text'] = 'Station mag niet leeg zijn'
                return False

            if bericht == '':
                self.label['text'] = 'Bericht mag niet leeg zijn'
                return False
            return True

        def plaatsen(ber_id, naam, stat_id, bericht, status, datum, tijd):
            cur.execute(
                'insert into bericht (bericht_id, naam, stat_id, bericht, status, datum, tijd) values (%s, '
                '%s, %s, %s, %s, %s, %s)',
                (ber_id, naam, stat_id, bericht, status, datum, tijd))
            bericht.strip('\n')
            print(
                f"Bericht \033[1m{ber_id}\033[0m bevat \033[1m{bericht}\033[0m is \033[1m{status}\033[0m en "
                f"opgeslagen op \033[1m{datum}\033[0m, \033[1m{tijd}\033[0m")
            con.commit()

        def verzamel():
            ber_id = idfinder()
            naam = identificatie(self.naaminvoer.get())

            station = self.station.get()
            cur.execute('select stat_id from station where naam = %s', (station,)), con.commit()
            data = cur.fetchall()

            status = 'pending'
            bericht = self.bericht.get('1.0', 'end')
            datum = datetime.now().strftime("%b %d %Y")
            tijd = datetime.now().strftime("%H:%M:%S")
            if verificatie(station, bericht):
                plaatsen(ber_id, naam, data[0][0], bericht, status, datum, tijd)
                self.label['text'] = '"Gelukt!\nUw inbreng is ingezonden.\nFijne dag!"'
                self.back['text'] = 'Ga Terug'

        root.title("Recensie")

        self.reactieframe = Frame(master=root, background='#f7d417')
        self.reactieframe.pack(fill='both', expand=True)

        self.label = Label(master=self.reactieframe,
                           text='"Welkom, {}!"'.format(identificatie(self.naaminvoer.get())),
                           foreground='#003373',
                           font=('Sans', 16, 'bold'),
                           background='#f7d417',
                           padx=10,
                           pady=5)
        self.label.pack(side=LEFT)

        self.infostat = Label(master=self.reactieframe,
                              text='1. "Op welk station bevindt u zich?"',
                              font=('Sans', 12, 'bold italic'),
                              background='#f7d417',
                              foreground='#003373',
                              padx=10,
                              pady=5)
        self.infostat.pack(padx=10, pady=5, fill=X)

        self.station = Entry(master=self.reactieframe)
        self.station.pack(padx=10, pady=5, fill=X)

        self.infobericht = Label(master=self.reactieframe,
                                 text='2. "Wat is uw ervaring van onze goederen en/of diensten?"',
                                 font=('Sans', 12, 'bold italic'),
                                 background='#f7d417',
                                 foreground='#003373',
                                 padx=10,
                                 pady=5)
        self.infobericht.pack(padx=10, pady=5, fill=X)

        self.bericht = Text(master=self.reactieframe, width=5, height=5)
        self.bericht.pack(padx=10, pady=5, fill=X)

        self.plaatsbericht = Button(master=self.reactieframe, text='Plaats Bericht', command=verzamel)
        self.plaatsbericht.pack(padx=10, pady=2, fill=X)

        self.back = Button(master=self.reactieframe, text='Annuleer', foreground='red', command=gotomain)
        self.back.pack(side='bottom', padx=10, pady=2, fill=X)


class ModeratieModule(Frame):  # Module | MODERATIE EN TWITTER API
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.loginmod()

    def inloggen(self):
        lijstje = []
        try:
            cur.execute('select * from moderator')
            data = cur.fetchall()
            for n in data:
                lijstje.append(n)
            return lijstje
        except:
            self.label['text'] = 'Er zijn geen moderators beschikbaar!'

    def pwcheck(self):
        for moderator in self.inloggen():
            if moderator in self.inloggen():
                if self.namefield.get() == moderator[1]:
                    if self.passfield.get() == moderator[2]:
                        self.geefmoderate()
            else:
                showinfo(title='Fout', message='Ongeldige Combinatie!')

    def geefloginframe(self):
        self.modframe.pack_forget()
        self.loginmod()

    def geefmoderate(self):
        self.loginframe.pack_forget()
        self.moderate()

    def loginmod(self):  # SQL Control | LOG IN
        def gotomain():  # Return naar HOOFDMENU
            self.loginframe.pack_forget()
            StartScherm()

        root.title('Log In')
        self.loginframe = Frame(master=root, background='#f7d417')
        self.loginframe.pack(fill='both', expand=True)

        self.label = Label(master=self.loginframe,
                           text='Moderatie Module',
                           foreground='#003373',
                           font=('Sans', 16, 'bold'),
                           background='#f7d417',
                           padx=10,
                           pady=5)
        self.label.pack(side=LEFT, padx=15)

        self.userlabel = Label(master=self.loginframe, text='Gebruikersnaam', background='#f7d417',
                               foreground='#003373')
        self.userlabel.pack(padx=5, pady=1, fill=X)

        self.namefield = Entry(master=self.loginframe)
        self.namefield.pack(padx=10, pady=2, fill=X)

        self.passlabel = Label(master=self.loginframe, text='Wachtwoord', background='#f7d417', foreground='#003373')
        self.passlabel.pack(padx=5, pady=1, fill=X)

        self.passfield = Entry(master=self.loginframe)
        self.passfield.pack(padx=10, pady=2, fill=X)

        self.loginbut = Button(master=self.loginframe,
                               text='Log In',
                               command=self.pwcheck)
        self.loginbut.pack(padx=10, pady=2, fill=X)

        self.back = Button(master=self.loginframe,
                           text='Terug',
                           foreground='red',
                           command=gotomain)
        self.back.pack(side='bottom', padx=10, pady=2, fill=X)

    def moderate(self):  # SQL Control | SQL DATA CONTROL
        def gotomain():  # Return naar HOOFDMENU
            self.modframe.pack_forget()
            StartScherm()

        bericht = []
        stationnetje = []
        moderator = []

        def ophalen():
            bericht.clear()
            stationnetje.clear()
            moderator.clear()
            try:
                cur.execute('select * from bericht where status = \'pending\'  order by datum, tijd'), con.commit()
                data = cur.fetchall()
                for n in data:
                    bericht.append(n)

                cur.execute('select * from station where stat_id = %s', (bericht[0][2],)), con.commit()
                data = cur.fetchall()
                for x in data:
                    stationnetje.append(x)
                self.comment["text"] = '{}\n{}\n\n{}\n\n{} | {}'.format(bericht[0][1], stationnetje[0][1],
                                                                        bericht[0][3],
                                                                        bericht[0][6], bericht[0][7])
            except:
                self.comment['text'] = 'Er zijn geen comments om te modereren!'

        def goedkeuren():
            name = self.namefield.get()
            cur.execute('select mod_id from moderator where naam = %s', (name,))
            con.commit()
            data = cur.fetchall()
            try:
                cur.execute('update bericht set status = %s where bericht_id = %s;', ('approved', bericht[0][0]))
                con.commit()
                cur.execute('update bericht set mod_id = %s where bericht_id = %s', (data[0][0], bericht[0][0]))
                con.commit()

                print(f'\t{bericht[0][0]} approved')
                self.label["text"] = "Approved"
                posten(bericht)
                ophalen()
            except IndexError:
                print("\n\tEr zijn geen comment om te modereren, dus indexerror is vermeden")

        def afkeuren():
            name = self.namefield.get()
            cur.execute('select mod_id from moderator where naam = %s', (name,))
            con.commit()
            data = cur.fetchall()
            try:
                cur.execute('update bericht set status = %s where bericht_id = %s;', ('rejected', bericht[0][0]))
                con.commit()
                cur.execute('update bericht set mod_id = %s where bericht_id = %s', (data[0][0], bericht[0][0]))
                con.commit()

                print(f'{bericht[0][0]} rejected')
                self.label["text"] = "Rejected"
                con.commit()
                ophalen()
            except IndexError:
                print("\n\tEr zijn geen comment om te modereren, dus indexerror is vermeden")

        def posten(lijstje):
            """
            bearer_token = AAAAAAAAAAAAAAAAAAAAANjGVQEAAAAAzfmYdFckYBqgZ4VpCuAvmJCW3FA%3DnqVfcs0iK3a3My66P9rjAdO1D8kkuScXr9EF9LprAcfBaJFZNH
            consumer_key = grnNCwC8u7UXCQp2NgXXA6WrV
            consumer_secret = 3XaMNA9CYiUGo4JhLGhwHnl5wG1OsptzNgBSGl7IwOoIBQOkqT
            access_token_key = 1439864860565704705-a43RJriHaWf06eaOFpVMIxiuV5aSJE
            access_token_secret = fZPWMLE0eIgn2O74O4lylQNBk8jQ4lIunlkNIXZlgEddm
            """

            stationnetje.clear()
            naam = lijstje[0][1]
            cur.execute('select * from station where stat_id = %s', (lijstje[0][2],))
            con.commit()
            data = cur.fetchall()
            for x in data:
                stationnetje.append(x)
            bericht = lijstje[0][3]

            auth = tweepy.OAuthHandler('grnNCwC8u7UXCQp2NgXXA6WrV',
                                       '3XaMNA9CYiUGo4JhLGhwHnl5wG1OsptzNgBSGl7IwOoIBQOkqT')
            auth.set_access_token('1439864860565704705-a43RJriHaWf06eaOFpVMIxiuV5aSJE',
                                  'fZPWMLE0eIgn2O74O4lylQNBk8jQ4lIunlkNIXZlgEddm')
            api = tweepy.API(auth)
            api.update_status(f'{naam} | {stationnetje[0][1]}\n{bericht}')

            return "bericht gepost"

        root.title('Free Speech Inc.')
        self.modframe = Frame(master=root, background='#f7d417')
        self.modframe.pack(fill='both', expand=True)

        self.label = Label(master=self.modframe, text='Moderatie\nModule', foreground='#003373',
                           font=('Sans', 16, 'bold'), background='#f7d417', padx=10, pady=5)
        self.label.pack(side=LEFT, padx=15)

        self.comment = Label(master=self.modframe, text='bruh', foreground='#003373', font=('Sans', 12),
                             background='#f7d417', padx=10, pady=10)
        self.comment.pack(side=RIGHT, padx=15)
        ophalen()

        self.goed = Button(master=self.modframe, text='Approve', command=goedkeuren)
        self.goed.pack(padx=10, pady=2, fill=X)

        self.false = Button(master=self.modframe, text='Deny', command=afkeuren)
        self.false.pack(padx=10, pady=2, fill=X)

        self.back = Button(master=self.modframe, text='Uitloggen', foreground='red', command=gotomain)
        self.back.pack(side='bottom', padx=10, pady=2, fill=X)


# TODO Overzicht Rejected | Optioneel

class SchermModule(Frame):  # Module | WEER API
    pass  # TODO Weer API | optioneel


class SqlControl(Frame):  # Module | SQL Database Control
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.loginsql()

    def inloggen(self):
        lijstje = []
        try:
            cur.execute('select * from moderator')
            data = cur.fetchall()
            for n in data:
                lijstje.append(n)
            return lijstje
        except:
            self.labelsettings['text'] = 'Er zijn geen admins beschikbaar!'

    def pwcheck(self):
        for moderator in self.inloggen():
            if moderator in self.inloggen():
                if self.userfieldsettings.get() == moderator[1] and self.passfieldsettings.get() == moderator[2]:
                    self.geefsqlcontrol()
            else:
                showinfo(title='Fout', message='Ongeldige Combinatie!')

    def geefloginframe(self):
        self.sqlframe.pack_forget()
        self.loginsql()

    def geefsqlcontrol(self):
        self.loginframe.pack_forget()
        self.sqlcontrol()

    def loginsql(self):  # SQL Control | LOG IN
        def gotomain():  # Return naar HOOFDMENU
            self.loginframe.pack_forget()
            StartScherm()

        root.title('Voer wachtwoord in')
        self.loginframe = Frame(master=root, background='#f7d417')
        self.loginframe.pack(fill='both', expand=True)

        self.labelsettings = Label(master=self.loginframe, text='SQL Control', foreground='#003373',
                                   font=('Sans', 16, 'bold'), background='#f7d417', padx=10, pady=5)
        self.labelsettings.pack(side=LEFT, padx=15)

        self.userlabelsettings = Label(master=self.loginframe, text='Gebruikersnaam', background='#f7d417',
                                       foreground='#003373')
        self.userlabelsettings.pack(padx=5, pady=1, fill=X)

        self.userfieldsettings = Entry(master=self.loginframe)
        self.userfieldsettings.pack(padx=10, pady=2, fill=X)

        self.passlabelsettings = Label(master=self.loginframe, text='Wachtwoord', background='#f7d417',
                                       foreground='#003373')
        self.passlabelsettings.pack(padx=5, pady=1, fill=X)

        self.passfieldsettings = Entry(master=self.loginframe)
        self.passfieldsettings.pack(padx=10, pady=2, fill=X)

        self.loginbutsettings = Button(master=self.loginframe, text='Log In', command=self.pwcheck)
        self.loginbutsettings.pack(padx=10, pady=2, fill=X)

        self.backsettings = Button(master=self.loginframe, text='Terug', foreground='red',
                                   command=gotomain)
        self.backsettings.pack(side='bottom', padx=10, pady=2, fill=X)

    def sqlcontrol(self):  # SQL Control | SQL DATA CONTROL
        def gotomain():  # Return naar HOOFDMENU
            self.sqlframe.pack_forget()
            StartScherm()

        root.title('Systeeminstellingen')
        self.sqlframe = Frame(master=root, background='#f7d417')
        self.sqlframe.pack(fill='both', expand=True)

        self.labelsettings = Label(master=self.sqlframe, text='SQL\nDatabase Control', foreground='#003373',
                                   font=('Sans', 16, 'bold'), background='#f7d417', padx=10, pady=5)
        self.labelsettings.pack(side=LEFT, padx=15)

        self.fill = Button(master=self.sqlframe, text='Vul database', command=opvulling)
        self.fill.pack(padx=10, pady=2, fill=X)

        self.allcases = Button(master=self.sqlframe, text='Verwijder alle instanties', command=deleteall)
        self.allcases.pack(padx=10, pady=2, fill=X)

        self.falsecases = Button(master=self.sqlframe, text='Verwijder afgewezen instanties', command=deletefalse)
        self.falsecases.pack(padx=10, pady=2, fill=X)

        self.backsettings = Button(master=self.sqlframe, text='Uitloggen', foreground='red', command=gotomain)
        self.backsettings.pack(side='bottom', padx=10, pady=2, fill=X)


class StartScherm(Frame):  # HOOFDMENU
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.navigation()

    def safeexit(self):
        cur.close()
        print('\n\tCursor Closed')
        con.close()
        print('\tDatabase Connection Closed')
        root.destroy()
        print('\tTkinter Closed')

    def navigation(self):
        def gotoreactie():
            self.startframe.pack_forget()
            ReactieModule()

        def gotosqlcontrol():
            self.startframe.pack_forget()
            SqlControl()

        def gotomoderatie():
            self.startframe.pack_forget()
            ModeratieModule()

        root.title('PROJA')

        self.startframe = Frame(master=root, background='#f7d417')
        self.startframe.pack(fill='both', side='top', expand=True)

        self.label = Label(master=self.startframe, text='NS Consumentenzuil', foreground='#003373',
                           font=('Sans', 16, 'bold'),  # bold, italic
                           background='#f7d417', padx=10, pady=5)
        self.label.pack(side=LEFT, padx=15)

        self.reageer = Button(master=self.startframe, text='Reageermodule', command=gotoreactie)
        self.reageer.pack(padx=10, pady=2, fill=X)

        self.moderatie = Button(master=self.startframe, text='Moderatiemodule', command=gotomoderatie)
        self.moderatie.pack(padx=10, pady=2, fill=X)

        self.control = Button(master=self.startframe, text='SQL Control', command=gotosqlcontrol)
        self.control.pack(padx=10, pady=2, fill=X)

        self.exit = Button(master=self.startframe, text="Exit", foreground="red", command=self.safeexit)
        self.exit.pack(side="bottom", fill=X, padx=10, pady=2)


if __name__ == '__main__':
    root = Tk()
    zuil = StartScherm(master=root)
    zuil.mainloop()
