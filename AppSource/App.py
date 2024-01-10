import InterfaceConnector

class App:

    NAME = 'DepotApp'
    VERSION = '0.2.23.12' #wydanie.wersja.rok.miesiac

    def __init__(self) -> None:
        pass
    def Run(self):
        while(True):
            ThisInterface = InterfaceConnector.Interface()
            ThisInterface.show_depot_init_menu()
            ThisInterface.show_operating_lines()
            ThisInterface.program_one_by_one()
            input()

    def Quit(self):
        self.QUIT = -1
        return self.QUIT
    
    def Info(self):
        txt = 'Program {}, wersja {}.\n.'
        print(txt.format(self.NAME, self.VERSION))


if __name__ == '__main__':
    app = App()
    app.Run()