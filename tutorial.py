import sqlite3, os, time, winsound

class Manager:
    def __init__(self):
        self.name = ''
        self.phone = ''
        self.address = ''

    def add(self):
        pass
    
    def update(self):
        pass

    def remove(self):
        pass

    def get_list(self):
        pass

    def terminate(self):
        pass

    def menu(self):
        os.system("cls")                        #clean screen

        print('-----------------MENU-----------------')
        print('1 - Add')
        print('2 - Update')
        print('3 - Remove')
        print('4 - List')
        print('5 - End')        
        print()

    def main(self):
        self.menu()

contacts_manager = Manager()
contacts_manager.main()