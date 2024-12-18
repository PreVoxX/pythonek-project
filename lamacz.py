import sys
import os
from time import sleep

class Cracker():
    def __init__(self,file,login,params_names):
        self.file_name = file
        if os.path.exists(file):
            print("file located!")
            #start czytania pliku
            self.passes = self.read_data(self.file_name)
            print("Data correctly loeaded!")
            print(self.passes)

             # zapisujemy login, gdy jest on stały podczas całego "szukania" hasła
            self.login = login
            if len(login) == 0:
                print("login not specified!")
                sys.exit()

            #przygotowujemy dane do wysłania
            try:
                self.data = []
                for pas in self.passes:
                    self.data.append((params_names[0], self.login, params_names[1], pas))
                    print("data correctly prepared!")
                    print(self.data)

            except IndexError:
                print("Params names specified incorreclty! ")
                sys.exit()


        else:
            print("file couldn't be founded")
            sys.exit()

       

    def read_data(self, filename):
        with open(filename, 'r')as f:
            lines = f.read().split('\n')
            return lines

craker = Cracker ("passes.txt", "login")